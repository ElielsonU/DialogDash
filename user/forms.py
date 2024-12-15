from typing import Any
from django.forms import ModelForm, TextInput, PasswordInput, CharField, ValidationError
from django.contrib.auth.hashers import make_password
from . import models

class UserForm(ModelForm):
  confirm_password = CharField(widget=PasswordInput(attrs={ 'placeholder': 'Confirme sua Senha' })) 
  class Meta:
    model = models.User
    fields = ['username', 'email', 'password']
    widgets = {
      'username': TextInput(attrs={ 'placeholder': 'Nome de usuário' }),
      'email': TextInput(attrs={ 'placeholder': 'Email' }),
      'password': PasswordInput(attrs={ 'placeholder': 'Senha' }),
    }

  def save(self, commit=True): 
    user = super().save(commit=False) 
    user.password = make_password(self.cleaned_data['password']) 
    if commit: user.save(commit) 
    return user

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    if password != confirm_password:
      raise ValidationError('As senhas não correspondem.')

    return cleaned_data