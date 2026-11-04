from django.contrib.auth.decorators import login_not_required, login_required
from django.shortcuts import redirect, render

from .forms import PublicSignUpForm


@login_required
def inicio(request):
    return render(
        request,
        'index.html'
    )


@login_not_required
def cadastro(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    form = PublicSignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        usuario = form.save(commit=False)
        usuario.is_active = False
        usuario.save()
        return redirect('cadastro_pendente')

    return render(request, 'registration/cadastro.html', {'form': form})


@login_not_required
def cadastro_pendente(request):
    return render(request, 'registration/cadastro_pendente.html')

def acesso_negado(request, exception):
    return render(request, '403.html', status=403)