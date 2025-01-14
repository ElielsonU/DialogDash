from django import forms
from .models import Chat, Participant
from user.models import User

class ChatForm(forms.ModelForm):
    email = forms.EmailField(label='Email do contato', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    creator = User()

    def __init__(self, *args, **kwargs):
        super(ChatForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ''
        self.fields['description'].required = False

    def save(self):
        chat = super().save(commit=False)
        chat.max_size = 2
        chat.type = "CVS"
        contact = User.objects.filter(email=self.cleaned_data['email']).first()
        if (not contact): 
             raise Exception("Usuário não encontrado")

        chat.save()
        Participant(chat=chat, user=contact).save()
        Participant(chat=chat, user=self.creator).save()

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