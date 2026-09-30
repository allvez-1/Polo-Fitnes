from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models.deletion import ProtectedError

from .forms import InstrutorForm
from .models import Instrutor


@login_required
def lista(request):
    return render(request, 'crud/lista.html', {'objetos': Instrutor.objects.all(), 'titulo': 'Instrutores', 'criar_url': 'instrutor:criar', 'editar_url': 'instrutor:editar', 'excluir_url': 'instrutor:excluir', 'detalhes_url': 'instrutor:detalhes'})


@login_required
@permission_required('instrutor.add_instrutor', raise_exception=True)
def criar(request):
    form = InstrutorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('instrutor:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar instrutor'})


@login_required
@permission_required('instrutor.change_instrutor', raise_exception=True)
def editar(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)
    form = InstrutorForm(request.POST or None, instance=instrutor)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('instrutor:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar instrutor'})


@login_required
@permission_required('instrutor.delete_instrutor', raise_exception=True)
def excluir(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)
    if request.method == 'POST':
        try:
            instrutor.delete()
        except ProtectedError:
            return render(request, 'crud/confirmar_exclusao.html', {
                'objeto': instrutor, 'titulo': 'Excluir instrutor',
                'erro': 'Este instrutor possui treinos associados e não pode ser excluído.',
            })
        else:
            return redirect('instrutor:lista')
    return render(request, 'crud/confirmar_exclusao.html', {'objeto': instrutor, 'titulo': 'Excluir instrutor'})

@login_required
def detalhes(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)

    campos = [
        ('Nome', instrutor.nome),
        ('CPF', instrutor.cpf),
        ('Especialidade', instrutor.especialidade),
        ('CREF', instrutor.cref),
        ('Ativo', 'Sim' if instrutor.ativo else 'Não'),
    ]

    return render(request, 'crud/detalhes.html', {
        'objeto': instrutor,
        'campos': campos,
        'titulo': 'Detalhes do instrutor',
    })
