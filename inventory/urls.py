from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login2.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('produtos/', views.ProdutoListView.as_view(), name='lista_produtos'),
    path('produtos/cadastrar/', views.ProdutoCreateView.as_view(), name='cadastrar_produto'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='editar_produto'),
    path('produtos/<int:pk>/exluir/', views.ProdutoDeleteView.as_view(), name='excluir_produto'),
    path('movimentacao/', views.MovimentacaoCreateView.as_view(), name='registrar_movimentacao'),
    path('produtos/historico_movimentacoes/', views.HistoricoMovimentacoesView.as_view(), name='historico_movimentacoes'),
]
