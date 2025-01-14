from django.shortcuts import redirect
from django.shortcuts import render, HttpResponse
from .models import Chat, Message
from .forms import ChatForm


# Create your views here.
def index(request):
  search = request.GET.get('search', "")
  
  chats = Chat.objects.filter(participant__user=request.user)
  if (search):
    chats = chats.filter(subject__icontains=search)

  context = {
    "chats": chats,
    "search": search
  }

  return render(request, "html/home.html", context=context)


def add_chat(request):
  if request.method == "POST":
    form = ChatForm(request.POST)
    if (form.is_valid()):
      form.creator = request.user
      try:
        form.save()
        return redirect('chats')
      except: pass
  else:
    form = ChatForm()
  
  context = {
    'form': form
  }

  return render(request, "html/add-chat.html", context=context)

def chat(request, id):
  chat = Chat.objects.filter(id=id).first()
  if (not chat):
    return redirect('chats')

  context = {
    'chat': Chat.objects.get(id=id),
    'messages': Message.objects.filter(chat=chat)
  }

  return render(request, "html/chat.html", context=context)

def delete_chat(request, id):
  chat = Chat.objects.filter(id=id).first()
  if (id != 9 and chat): 
    chat.delete()
  return redirect('chats')