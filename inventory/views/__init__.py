# Import FBVs from llcaoafbls modulfodule
from .fbvs import home, registrar_usuario, lista_produtos, cadastrar_produto, editar_produto, excluir_produto, registrar_movimentacao, historico_movimentacoes

# Import CBVs from separate modules
from .produtos import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView
from .usuarios import HomeView, RegisterView
from .movimentacoes import MovimentacaoCreateView, HistoricoMovimentacoesView

__all__ = [
    # FBVs
    'home', 'registrar_usuario', 'lista_produtos', 'cadastrar_produto', 'editar_produto', 'excluir_produto', 'registrar_movimentacao', 'historico_movimentacoes',
    # CBVs
    'ProdutoListView', 'ProdutoCreateView', 'ProdutoUpdateView', 'ProdutoDeleteView',
    'HomeView', 'RegisterView', 'MovimentacaoCreateView', 'HistoricoMovimentacoesView',
]
