from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExercicioForm
from .models import Exercicio


@login_required
def lista(request):
    return render(
        request,
        'crud/lista.html',
        {
            'objetos': Exercicio.objects.all(),
            'titulo': 'Exercícios',
            'criar_url': 'exercicios:criar',
            'editar_url': 'exercicios:editar',
            'excluir_url': 'exercicios:excluir',
            'detalhes_url': 'exercicios:detalhes',
        }
    )


@login_required
@permission_required('exercicios.add_exercicio', raise_exception=True)
def criar(request):
    form = ExercicioForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'exercicios:lista'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Cadastrar exercício'
        }
    )


@login_required
@permission_required('exercicios.change_exercicio', raise_exception=True)
def editar(request, pk):
    exercicio = get_object_or_404(
        Exercicio,
        pk=pk
    )

    form = ExercicioForm(
        request.POST or None,
        instance=exercicio
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect(
            'exercicios:lista'
        )

    return render(
        request,
        'crud/formulario.html',
        {
            'form': form,
            'titulo': 'Editar exercício'
        }
    )


@login_required
@permission_required('exercicios.delete_exercicio', raise_exception=True)
def excluir(request, pk):
    exercicio = get_object_or_404(
        Exercicio,
        pk=pk
    )

    if request.method == 'POST':
        exercicio.delete()

        return redirect(
            'exercicios:lista'
        )

    return render(
        request,
        'crud/confirmar_exclusao.html',
        {
            'objeto': exercicio,
            'titulo': 'Excluir exercício'
        }
    )


@login_required
def detalhes(request, pk):
    exercicio = get_object_or_404(
        Exercicio,
        pk=pk
    )

    campos = [
        ('Nome', exercicio.nome),
        ('Grupo muscular', exercicio.grupo_muscular),
        ('Equipamento', exercicio.equipamento),
        ('Ativo', 'Sim' if exercicio.ativo else 'Não'),
    ]

    return render(
        request,
        'crud/detalhes.html',
        {
            'objeto': exercicio,
            'campos': campos,
            'titulo': 'Detalhes do exercício',
        }
    )
