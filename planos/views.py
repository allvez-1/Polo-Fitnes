from django.shortcuts import get_object_or_404, redirect, render
from django.db.models.deletion import ProtectedError

from .forms import PlanoForm
from .models import Plano


def lista(request):
    return render(request, 'crud/lista.html', {'objetos': Plano.objects.all(), 'titulo': 'Planos', 'criar_url': 'planos:criar', 'editar_url': 'planos:editar', 'excluir_url': 'planos:excluir'})


def criar(request):
    form = PlanoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('planos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar plano'})


def editar(request, pk):
    plano = get_object_or_404(Plano, pk=pk)
    form = PlanoForm(request.POST or None, instance=plano)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('planos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar plano'})


def excluir(request, pk):
    plano = get_object_or_404(Plano, pk=pk)
    if request.method == 'POST':
        try:
            plano.delete()
        except ProtectedError:
            return render(request, 'crud/confirmar_exclusao.html', {
                'objeto': plano, 'titulo': 'Excluir plano',
                'erro': 'Este plano possui alunos associados e não pode ser excluído.',
            })
        else:
            return redirect('planos:lista')
    return render(request, 'crud/confirmar_exclusao.html', {'objeto': plano, 'titulo': 'Excluir plano'})
