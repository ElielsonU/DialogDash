from django.urls import path, resolve
from . import views

urlpatterns = [
  path("", views.index)
]