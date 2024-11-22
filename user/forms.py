from django.forms import ModelForm, TextInput, PasswordInput, CharField, ValidationError
from . import models

class UserForm(ModelForm):
  confirm_password = CharField(widget=PasswordInput(attrs={ 'placeholder': 'Confirme sua Senha' })) 
  class Meta:
    model = models.User
    fields = ['username', 'email', 'password']
    widgets = {
      'username': TextInput(attrs={ 'placeholder': 'Nome de usuário' }),
      'email': TextInput(attrs={ 'placeholder': 'Email' }),
      'password': TextInput(attrs={ 'placeholder': 'Senha' }),
    }

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    if password != confirm_password:
      raise ValidationError('As senhas não correspondem.')

    return cleaned_data