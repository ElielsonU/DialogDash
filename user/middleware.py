from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.core.cache import cache

auth_paths = ['/user/login/', '/user/signup/']

class AuthMiddleware:
    cache.clear()
    def __init__(self, get_response: callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.user.is_authenticated:
            if request.path in auth_paths:
                return redirect('index')
        elif request.path not in auth_paths:
            return redirect('user.login')
        return self.get_response(request)        

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
