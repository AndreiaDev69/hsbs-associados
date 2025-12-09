
from django.contrib import admin
from .models import Associado, LancamentoFinanceiro, MovimentoAuditoria

@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'documento', 'email', 'status')
    list_filter = ('status',)
    search_fields = ('nome', 'documento', 'email')
    filter_horizontal = ('usuarios',)

@admin.register(LancamentoFinanceiro)
class LancamentoFinanceiroAdmin(admin.ModelAdmin):
    list_display = ('associado', 'tipo', 'descricao', 'valor', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('descricao', 'associado__nome')

@admin.register(MovimentoAuditoria)
class MovimentoAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('associado', 'acao', 'usuario', 'data_hora')
    list_filter = ('acao', 'data_hora')
    search_fields = ('associado__nome', 'acao', 'detalhes')
