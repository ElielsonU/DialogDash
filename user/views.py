from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render
from . import forms, models

# Create your views here.

def index(request):
    return HttpResponse("dasdasdas")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = models.User.objects.get(email=email)

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('chat')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'html/login.html')

def signup_view(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return login_view(request)
    return render(request, 'html/signup.html', { 'form': form })