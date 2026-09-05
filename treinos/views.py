from django.shortcuts import get_object_or_404, redirect, render

from .forms import TreinoForm
from .models import Treino


def lista(request):
    return render(request, 'crud/lista.html', {
        'objetos': Treino.objects.select_related('aluno', 'instrutor').all(), 'titulo': 'Treinos',
        'criar_url': 'treinos:criar', 'editar_url': 'treinos:editar',
        'excluir_url': 'treinos:excluir',
    })


def criar(request):
    form = TreinoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('treinos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar treino'})


def editar(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    form = TreinoForm(request.POST or None, instance=treino)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('treinos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar treino'})


def excluir(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    if request.method == 'POST':
        treino.delete()
        return redirect('treinos:lista')
    return render(request, 'crud/confirmar_exclusao.html', {'objeto': treino, 'titulo': 'Excluir treino'})
