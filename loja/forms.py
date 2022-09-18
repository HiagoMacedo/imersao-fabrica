from django.forms import ModelForm
from loja.models import Produto, Pedido

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'valor']
        
        
class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cpf', 'endereco', 'prazoEntrega', 'codigoProduto']
        
        