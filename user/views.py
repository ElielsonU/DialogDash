from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return HttpResponse("dasdasdas")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
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
    print(form)
    return render(request, 'html/signup.html', { 'form': form })