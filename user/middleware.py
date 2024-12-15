from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse

auth_paths = ['/user/login/', '/user/signup/']

class AuthMiddleware:
    def __init__(self, get_response: callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.user.is_authenticated:
            if request.path in auth_paths:
                return redirect('index')
        elif request.path not in auth_paths:
            return redirect('usuarios:login')
        return self.get_response(request)        

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
