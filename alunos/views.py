from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoForm
from .models import Aluno


@login_required
def lista(request):
    return render(request, 'crud/lista.html', {
        'objetos': Aluno.objects.select_related('plano').all(), 'titulo': 'Alunos',
        'criar_url': 'alunos:criar', 'editar_url': 'alunos:editar',
        'excluir_url': 'alunos:excluir',
        'detalhes_url': 'alunos:detalhes',
    })


@login_required
@permission_required('alunos.add_aluno', raise_exception=True)
def criar(request):
    form = AlunoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alunos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar aluno'})


@login_required
@permission_required('alunos.change_aluno', raise_exception=True)
def editar(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alunos:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar aluno'})


@login_required
@permission_required('alunos.delete_aluno', raise_exception=True)
def excluir(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos:lista')
    return render(request, 'crud/confirmar_exclusao.html', {'objeto': aluno, 'titulo': 'Excluir aluno'})

@login_required
def detalhes(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    campos = [
        ('Nome', aluno.nome),
        ('CPF', aluno.cpf),
        ('Data de matrícula', aluno.data_matricula),
        ('Data de vencimento', aluno.data_vencimento),
        ('Ativo', 'Sim' if aluno.ativo else 'Não'),
        ('Plano', aluno.plano),
    ]

    return render(request, 'crud/detalhes.html', {
        'objeto': aluno,
        'campos': campos,
        'titulo': 'Detalhes do aluno',
    })
