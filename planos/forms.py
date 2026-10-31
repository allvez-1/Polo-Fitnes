from django import forms

from .models import Plano


class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano

        fields = [

            'nome',
            'valor',
            'duracao_dias',
            'ativo',
        ]

        