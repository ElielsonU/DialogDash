from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    email = forms.EmailField(label='Email do contato', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ChatForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ''
        self.fields['description'].required = False

    def save(self, *args, **kwargs):
      form = super(ChatForm, self).save(*args, **kwargs, commit=False)
      print(form)
      pass

    class Meta:
        model = Chat
        fields = ['subject', 'email', 'description']
        labels = {
           'subject': 'Nome',
           'description': 'Descrição',
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'},
            ),
        }