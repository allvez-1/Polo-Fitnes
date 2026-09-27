from django.shortcuts import render


def inicio(request):
    return render(
        request,
        'polo_fitnes.html'
    )