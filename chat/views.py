from django.shortcuts import render, HttpResponse
from .models import Chat
from .forms import ChatForm


# Create your views here.
def index(request):
  chats = Chat.objects.filter(participant__user=request.user)

  context = {
    "chats": chats
  }

  return render(request, "html/home.html", context=context)


def add_chat(request):
  if request.method == "POST":
    form = ChatForm(request.POST)
    if (form.is_valid()):
      chat = form.save()
      return HttpResponse(f"Chat criado com sucesso!")
  else:
    form = ChatForm()
  
  context = {
    'form': form
  }

  return render(request, "html/add-chat.html", context=context)