from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User

class FormularioEntrada(ModelForm):
   class Meta:
      model = Entrada

class FormularioComentario(ModelForm):
    class Meta:
        model = Comentario
        exclude = ["identrada"]


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AuthenticationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
