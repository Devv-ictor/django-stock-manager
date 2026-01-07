from django import forms
from django.contrib.auth.models import User
from .models import Produto, Movimentacao

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('As senhas não coincidem.')
        return cd.get('password2')

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'descricao', 'preco_unitario']
        widgets = {
            'preco_unitario': forms.NumberInput(attrs={'step': '0.01'})
        }

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade', 'observacao']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'min': '1'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.all()

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade <= 0:
            raise forms.ValidationError('Quantidade deve ser maior que zero')
        
        tipo = self.cleaned_data.get('tipo')
        produto = self.cleaned_data.get('produto')
        
        if tipo == 'SAIDA' and produto and quantidade > produto.quantidade:
            raise forms.ValidationError('Quantidade insuficiente em estoque')
        
        return quantidade
