from django.urls import path, resolve
from . import views

urlpatterns = [
  path("", views.index, name='chats'),
  path("add-chat", views.add_chat, name='add-chat'),
]