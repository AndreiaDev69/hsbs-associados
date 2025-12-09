
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Associado(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )

    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=20, blank=True, null=True)  # CPF/CNPJ
    telefone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    responsavel = models.CharField(max_length=255, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=30, blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    usuarios = models.ManyToManyField(
        User,
        related_name='associados_vinculados',
        blank=True,
        help_text='Usuários que são ADM deste associado'
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class LancamentoFinanceiro(models.Model):
    TIPO_CHOICES = (
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    )

    associado = models.ForeignKey(Associado, on_delete=models.CASCADE, related_name='lancamentos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.associado.nome} - {self.tipo} - {self.valor}"


class MovimentoAuditoria(models.Model):
    associado = models.ForeignKey(Associado, on_delete=models.CASCADE, related_name='movimentos')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    acao = models.CharField(max_length=50)  # CRIAR, EDITAR, EXCLUIR, LOGIN, UPLOAD etc
    detalhes = models.TextField(blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.associado.nome} - {self.acao} em {self.data_hora:%d/%m/%Y %H:%M}"
