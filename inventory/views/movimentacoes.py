from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from ..models import Produto, Movimentacao
from ..forms import MovimentacaoForm


class MovimentacaoCreateView(CreateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'registrar_movimentacao.html'
    success_url = reverse_lazy('lista_produtos')

    def form_valid(self, form):
        produto = form.cleaned_data['produto']
        tipo = form.cleaned_data['tipo']
        quantidade = form.cleaned_data['quantidade']

        if tipo == 'ENTRADA':
            produto.quantidade += quantidade
        else:
            produto.quantidade -= quantidade
        produto.save()

        return super().form_valid(form)


class HistoricoMovimentacoesView(LoginRequiredMixin, ListView):
    model = Movimentacao
    template_name = 'historico_movimentacoes.html'
    context_object_name = 'movimentacoes'
    login_url = 'login'

    def get_queryset(self):
        queryset = Movimentacao.objects.select_related('produto').order_by('-criado_em')
        produto_id = self.request.GET.get('produto', '')
        tipo = self.request.GET.get('tipo', '')
        data_inicio = self.request.GET.get('data_inicio', '')
        data_fim = self.request.GET.get('data_fim', '')

        if produto_id:
            queryset = queryset.filter(produto_id=int(produto_id))
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        if data_inicio:
            queryset = queryset.filter(criado_em__date__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(criado_em__date__lte=data_fim)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        context['filtros'] = {
            'produto_id': self.request.GET.get('produto', ''),
            'tipo': self.request.GET.get('tipo', ''),
            'data_inicio': self.request.GET.get('data_inicio', ''),
            'data_fim': self.request.GET.get('data_fim', ''),
        }
        return context
