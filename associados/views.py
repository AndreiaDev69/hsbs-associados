
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

from .models import Associado, LancamentoFinanceiro, MovimentoAuditoria
from .forms import AssociadoForm, LancamentoFinanceiroForm

def is_master(user):
    return user.is_superuser or user.groups.filter(name='master').exists()

def associados_queryset_para_usuario(user):
    if is_master(user):
        return Associado.objects.all()
    return Associado.objects.filter(usuarios=user)

@login_required
def inicio(request):
    return render(request, 'associados/inicio.html')

@login_required
def associados_list(request):
    associados = associados_queryset_para_usuario(request.user).order_by('nome')
    return render(request, 'associados/list.html', {'associados': associados})

@login_required
def associado_detalhes(request, pk):
    qs = associados_queryset_para_usuario(request.user)
    associado = get_object_or_404(qs, pk=pk)
    lancamentos = associado.lancamentos.all().order_by('-data')
    movimentos = associado.movimentos.all().order_by('-data_hora')
    return render(request, 'associados/detalhes.html', {
        'associado': associado,
        'lancamentos': lancamentos,
        'movimentos': movimentos,
    })

@login_required
def associado_create(request):
    if not is_master(request.user):
        return HttpResponseForbidden('Você não tem permissão para criar associados.')
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form.is_valid():
            associado = form.save()
            messages.success(request, 'Associado criado com sucesso.')
            return redirect('associados_list')
    else:
        form = AssociadoForm()
    return render(request, 'associados/form.html', {'form': form, 'titulo': 'Novo Associado'})

@login_required
def associado_edit(request, pk):
    qs = associados_queryset_para_usuario(request.user)
    associado = get_object_or_404(qs, pk=pk)
    if not (is_master(request.user) or request.user in associado.usuarios.all()):
        return HttpResponseForbidden('Você não tem permissão para editar este associado.')
    if request.method == 'POST':
        form = AssociadoForm(request.POST, instance=associado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Associado atualizado com sucesso.')
            return redirect('associado_detalhes', pk=associado.pk)
    else:
        form = AssociadoForm(instance=associado)
    return render(request, 'associados/form.html', {'form': form, 'titulo': 'Editar Associado'})

@login_required
def associado_delete(request, pk):
    qs = associados_queryset_para_usuario(request.user)
    associado = get_object_or_404(qs, pk=pk)
    if not is_master(request.user):
        return HttpResponseForbidden('Você não tem permissão para excluir associados.')
    if request.method == 'POST':
        associado.delete()
        messages.success(request, 'Associado excluído.')
        return redirect('associados_list')
    return render(request, 'associados/delete.html', {'associado': associado})

@login_required
def financeiro_associado(request, pk):
    qs = associados_queryset_para_usuario(request.user)
    associado = get_object_or_404(qs, pk=pk)
    if request.method == 'POST':
        form = LancamentoFinanceiroForm(request.POST)
        if form.is_valid():
            lanc = form.save(commit=False)
            lanc.associado = associado
            lanc.save()
            MovimentoAuditoria.objects.create(
                associado=associado,
                usuario=request.user,
                acao='LANÇAMENTO FINANCEIRO',
                detalhes=f'{lanc.tipo} - {lanc.descricao} - {lanc.valor}'
            )
            messages.success(request, 'Lançamento financeiro registrado.')
            return redirect('financeiro_associado', pk=associado.pk)
    else:
        form = LancamentoFinanceiroForm()
    lancamentos = associado.lancamentos.all().order_by('-data')
    return render(request, 'associados/financeiro.html', {
        'associado': associado,
        'form': form,
        'lancamentos': lancamentos,
    })

@login_required
def relatorios(request):
    return render(request, 'associados/relatorios.html')
