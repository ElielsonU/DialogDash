from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name='chats'),
  path("add-chat", views.add_chat, name='add-chat'),
  path("chat/<int:id>", views.chat, name='chat'),
]