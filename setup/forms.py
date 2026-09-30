from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class PublicSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')
        labels = {'username': 'Usuário'}
