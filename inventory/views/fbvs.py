from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from ..models import Produto, Movimentacao
from ..forms import ProdutoForm, MovimentacaoForm, UserRegisterForm


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'usuario': request.user})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registrar_usuario.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'registrar_usuario.html', {'form': form})

@login_required(login_url='login')
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
        
    return render(request, 'cadastrar_produto.html', {'form': form})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    
    return render(request, 'excluir_produto.html', {'produto': produto})

def registrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)

        if form.is_valid():
            produto = form.cleaned_data['produto']
            tipo = form.cleaned_data['tipo']
            quantidade = form.cleaned_data['quantidade']
            observacao = form.cleaned_data['observacao']

            movimentacao = Movimentacao.objects.create(
                produto=produto,
                tipo=tipo,
                quantidade=quantidade,
                observacao=observacao,
            )

            if tipo == 'ENTRADA':
                produto.quantidade += quantidade
            else:
                produto.quantidade -= quantidade
            produto.save()

            return redirect('lista_produtos')
    else:
        form = MovimentacaoForm()

    return render(request, 'registrar_movimentacao.html', {'form': form})

def historico_movimentacoes(request):
    movimentacoes = Movimentacao.objects.select_related('produto').order_by('-criado_em')
    produtos = Produto.objects.all()

    produto_id = request.GET.get('produto','')
    tipo = request.GET.get('tipo','')
    data_inicio = request.GET.get('data_inicio','')
    data_fim = request.GET.get('data_fim','')

    if produto_id:
        movimentacoes = movimentacoes.filter(produto_id=int(produto_id))
    if tipo:
        movimentacoes = movimentacoes.filter(tipo=tipo)
    if data_inicio:
        movimentacoes = movimentacoes.filter(criado_em__date__gte=data_inicio)
    if data_fim:
        movimentacoes = movimentacoes.filter(criado_em__date__lte=data_fim)
    return render(request, 'historico_movimentacoes.html', {
        'movimentacoes': movimentacoes,
        'produtos': produtos,
        'filtros': {
            'produto_id': produto_id,
            'tipo': tipo,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
        }
    })
