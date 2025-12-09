
from django import forms
from .models import Associado, LancamentoFinanceiro

class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = [
            'nome', 'documento', 'telefone', 'email', 'endereco',
            'responsavel', 'telefone_responsavel', 'status', 'usuarios'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'usuarios': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class LancamentoFinanceiroForm(forms.ModelForm):
    class Meta:
        model = LancamentoFinanceiro
        fields = ['tipo', 'descricao', 'valor', 'data']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
