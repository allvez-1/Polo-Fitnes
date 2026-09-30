from django.contrib.auth.decorators import login_required, permission_required
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

@login_required
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
            'detalhes_url': 'treinos:detalhes',
        }
    )


@login_required
@permission_required('treinos.add_treino', raise_exception=True)
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


@login_required
@permission_required('treinos.change_treino', raise_exception=True)
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


@login_required
@permission_required('treinos.delete_treino', raise_exception=True)
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


@login_required
def detalhes(request, pk):
    treino = get_object_or_404(
        Treino,
        pk=pk
    )

    alunos = ', '.join(
        str(relacao.aluno)
        for relacao in treino.alunos_treinos.select_related('aluno')
    ) or 'Nenhum aluno associado'
    exercicios = ', '.join(
        str(exercicio)
        for exercicio in treino.exercicios.all()
    ) or 'Nenhum exercício associado'

    campos = [
        ('Nome', treino.nome),
        ('Objetivo', treino.objetivo),
        ('Descrição', treino.descricao),
        ('Data de criação', treino.data_criacao),
        ('Instrutor', treino.instrutor),
        ('Alunos', alunos),
        ('Exercícios', exercicios),
    ]

    return render(
        request,
        'crud/detalhes.html',
        {
            'objeto': treino,
            'campos': campos,
            'titulo': 'Detalhes do treino',
        }
    )


# ==========================
# CRUD ALUNO TREINO
# ==========================

@login_required
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
            'detalhes_url': 'treinos:detalhes_aluno_treino',
        }
    )


@login_required
@permission_required('treinos.add_alunotreino', raise_exception=True)
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


@login_required
@permission_required('treinos.change_alunotreino', raise_exception=True)
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


@login_required
@permission_required('treinos.delete_alunotreino', raise_exception=True)
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


@login_required
def detalhes_aluno_treino(request, pk):
    aluno_treino = get_object_or_404(
        AlunoTreino,
        pk=pk
    )

    campos = [
        ('Aluno', aluno_treino.aluno),
        ('Treino', aluno_treino.treino),
        ('Data de início', aluno_treino.data_inicio),
        ('Data de fim', aluno_treino.data_fim),
        ('Ativo', 'Sim' if aluno_treino.ativo else 'Não'),
    ]

    return render(
        request,
        'crud/detalhes.html',
        {
            'objeto': aluno_treino,
            'campos': campos,
            'titulo': 'Detalhes do treino do aluno',
        }
    )


# ==========================
# CRUD TREINO EXERCICIO
# ==========================

@login_required
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
            'detalhes_url': 'treinos:detalhes_treino_exercicio',
        }
    )


@login_required
@permission_required('treinos.add_treinoexercicio', raise_exception=True)
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


@login_required
@permission_required('treinos.change_treinoexercicio', raise_exception=True)
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


@login_required
@permission_required('treinos.delete_treinoexercicio', raise_exception=True)
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


@login_required
def detalhes_treino_exercicio(request, pk):
    treino_exercicio = get_object_or_404(
        TreinoExercicio,
        pk=pk
    )

    campos = [
        ('Treino', treino_exercicio.treino),
        ('Exercício', treino_exercicio.exercicio),
        ('Ordem', treino_exercicio.ordem),
        ('Séries', treino_exercicio.series),
        ('Repetições', treino_exercicio.repeticoes),
        ('Carga (kg)', treino_exercicio.carga_kg),
        ('Descanso (segundos)', treino_exercicio.descanso_segundos),
        ('Observação', treino_exercicio.observacao),
    ]

    return render(
        request,
        'crud/detalhes.html',
        {
            'objeto': treino_exercicio,
            'campos': campos,
            'titulo': 'Detalhes do exercício do treino',
        }
    )
