from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExercicioForm
from .models import Exercicio


def lista(request):
    return render(request, 'crud/lista.html', {'objetos': Exercicio.objects.all(), 'titulo': 'Exercícios', 'criar_url': 'exercicios:criar', 'editar_url': 'exercicios:editar', 'excluir_url': 'exercicios:excluir'})


def criar(request):
    form = ExercicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('exercicios:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar exercício'})


def editar(request, pk):
    exercicio = get_object_or_404(Exercicio, pk=pk)
    form = ExercicioForm(request.POST or None, instance=exercicio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('exercicios:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar exercício'})


def excluir(request, pk):
    exercicio = get_object_or_404(Exercicio, pk=pk)
    if request.method == 'POST':
        exercicio.delete()
        return redirect('exercicios:lista')
    return render(request, 'crud/confirmar_exclusao.html', {'objeto': exercicio, 'titulo': 'Excluir exercício'})
