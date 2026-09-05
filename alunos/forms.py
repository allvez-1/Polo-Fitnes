from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'data_matricula', 'data_vencimento', 'ativo', 'plano']
        widgets = {
            'data_matricula': forms.DateInput(attrs={'type': 'date'}),
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
        }
