from django.forms import ModelForm
from . import models

class UserForm(ModelForm):
  class Meta:
    model = models.User
    fields = ['email', 'username' , 'password']