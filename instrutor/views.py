from django.shortcuts import get_object_or_404, redirect, render
from django.db.models.deletion import ProtectedError

from .forms import InstrutorForm
from .models import Instrutor


def lista(request):
    return render(request, 'crud/lista.html', {'objetos': Instrutor.objects.all(), 'titulo': 'Instrutores', 'criar_url': 'instrutor:criar', 'editar_url': 'instrutor:editar', 'excluir_url': 'instrutor:excluir'})


def criar(request):
    form = InstrutorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('instrutor:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Cadastrar instrutor'})


def editar(request, pk):
    instrutor = get_object_or_404(Instrutor, pk=pk)
    form = InstrutorForm(request.POST or None, instance=instrutor)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('instrutor:lista')
    return render(request, 'crud/formulario.html', {'form': form, 'titulo': 'Editar instrutor'})


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
