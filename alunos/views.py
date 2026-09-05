from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoForm
from .models import Aluno


def lista(request):
    return render(request, 'crud/lista.html', {
        'objetos': Aluno.objects.select_related('plano').all(), 'titulo': 'Alunos',
        'criar_url': 'alunos:criar', 'editar_url': 'alunos:editar',
        'excluir_url': 'alunos:excluir',
    })


def criar(request):
    form = AlunoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alunos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar aluno'})


def editar(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alunos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar aluno'})


def excluir(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos:lista')
    return render(request, 'crud/confirmar_exclusao.html', {'objeto': aluno, 'titulo': 'Excluir aluno'})
