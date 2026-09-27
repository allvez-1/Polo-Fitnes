from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    TreinoForm,
    AlunoTreinoForm,
    TreinoExercicioForm
)

from .models import (
    Treino,
    AlunoTreino,
    TreinoExercicio
)


# ==========================
# CRUD TREINO
# ==========================

def lista(request):
    treinos = Treino.objects.select_related(
        'instrutor'
    ).all()

    return render(
        request,
        'crud/lista.html',
        {
            'objetos': treinos,
            'titulo': 'Treinos',
            'criar_url': 'treinos:criar',
            'editar_url': 'treinos:editar',
            'excluir_url': 'treinos:excluir',
        }
    )


def criar(request):
    form = TreinoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'treinos:lista'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Cadastrar treino'
        }
    )


def editar(request, pk):
    treino = get_object_or_404(
        Treino,
        pk=pk
    )

    form = TreinoForm(
        request.POST or None,
        instance=treino
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'treinos:lista'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Editar treino'
        }
    )


def excluir(request, pk):
    treino = get_object_or_404(
        Treino,
        pk=pk
    )

    if request.method == 'POST':
        treino.delete()

        return redirect(
            'treinos:lista'
        )

    return render(
        request,
        'crud/confirmar_exclusao.html',
        {
            'objeto': treino,
            'titulo': 'Excluir treino'
        }
    )


# ==========================
# CRUD ALUNO TREINO
# ==========================

def lista_aluno_treino(request):
    objetos = AlunoTreino.objects.select_related(
        'aluno',
        'treino'
    ).all()

    return render(
        request,
        'crud/lista.html',
        {
            'objetos': objetos,
            'titulo': 'Treinos dos alunos',
            'criar_url': 'treinos:criar_aluno_treino',
            'editar_url': 'treinos:editar_aluno_treino',
            'excluir_url': 'treinos:excluir_aluno_treino',
        }
    )


def criar_aluno_treino(request):
    form = AlunoTreinoForm(
        request.POST or None
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'treinos:lista_aluno_treino'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Atribuir treino ao aluno'
        }
    )


def editar_aluno_treino(request, pk):
    aluno_treino = get_object_or_404(
        AlunoTreino,
        pk=pk
    )

    form = AlunoTreinoForm(
        request.POST or None,
        instance=aluno_treino
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'treinos:lista_aluno_treino'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Editar treino do aluno'
        }
    )


def excluir_aluno_treino(request, pk):
    aluno_treino = get_object_or_404(
        AlunoTreino,
        pk=pk
    )

    if request.method == 'POST':
        aluno_treino.delete()

        return redirect(
            'treinos:lista_aluno_treino'
        )

    return render(
        request,
        'crud/confirmar_exclusao.html',
        {
            'objeto': aluno_treino,
            'titulo': 'Remover treino do aluno'
        }
    )


# ==========================
# CRUD TREINO EXERCICIO
# ==========================

def lista_treino_exercicio(request):
    objetos = TreinoExercicio.objects.select_related(
        'treino',
        'exercicio'
    ).all()

    return render(
        request,
        'crud/lista.html',
        {
            'objetos': objetos,
            'titulo': 'Exercícios dos treinos',
            'criar_url': 'treinos:criar_treino_exercicio',
            'editar_url': 'treinos:editar_treino_exercicio',
            'excluir_url': 'treinos:excluir_treino_exercicio',
        }
    )


def criar_treino_exercicio(request):
    form = TreinoExercicioForm(
        request.POST or None
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'treinos:lista_treino_exercicio'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Adicionar exercício ao treino'
        }
    )


def editar_treino_exercicio(request, pk):
    treino_exercicio = get_object_or_404(
        TreinoExercicio,
        pk=pk
    )

    form = TreinoExercicioForm(
        request.POST or None,
        instance=treino_exercicio
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'treinos:lista_treino_exercicio'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Editar exercício do treino'
        }
    )


def excluir_treino_exercicio(request, pk):
    treino_exercicio = get_object_or_404(
        TreinoExercicio,
        pk=pk
    )

    if request.method == 'POST':
        treino_exercicio.delete()

        return redirect(
            'treinos:lista_treino_exercicio'
        )

    return render(
        request,
        'crud/confirmar_exclusao.html',
        {
            'objeto': treino_exercicio,
            'titulo': 'Remover exercício do treino'
        }
    )