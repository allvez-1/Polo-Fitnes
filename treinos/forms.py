from django import forms

from .models import Treino, AlunoTreino, TreinoExercicio


class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = [
            'nome',
            'objetivo',
            'descricao',
            'instrutor'
        ]


class AlunoTreinoForm(forms.ModelForm):
    class Meta:
        model = AlunoTreino
        fields = [
            'aluno',
            'treino',
            'data_inicio',
            'data_fim',
            'ativo'
        ]

        widgets = {
            'data_inicio': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'data_fim': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class TreinoExercicioForm(forms.ModelForm):
    class Meta:
        model = TreinoExercicio

        fields = [
            'treino',
            'exercicio',
            'ordem',
            'series',
            'repeticoes',
            'carga_kg',
            'descanso_segundos',
            'observacao'
        ]