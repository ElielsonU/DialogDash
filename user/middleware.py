from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse

auth_paths = ['/user/login/', '/user/signup/']

class AuthMiddleware:
    def __init__(self, get_response: callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.path not in auth_paths:
            if not request.user.is_authenticated:
                return redirect(reverse('user.login'))
            response: HttpResponse = self.get_response(request)
            return response
        
        if request.user.is_authenticated:
            return redirect(reverse('chat'))
        
        return self.get_response(request)

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
