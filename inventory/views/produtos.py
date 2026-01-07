from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Produto
from ..forms import ProdutoForm


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'
    login_url = 'login'


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastrar_produto.html'
    success_url = reverse_lazy('lista_produtos')


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'editar_produto.html'
    success_url = reverse_lazy('lista_produtos')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'excluir_produto.html'
    success_url = reverse_lazy('lista_produtos')
