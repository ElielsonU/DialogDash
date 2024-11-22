from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse

auth_paths = ['/user/login/', '/user/signup/']

class AuthMiddleware:
    def __init__(self, get_response: callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        print(request.user.is_authenticated)
        # if not request.user.is_authenticated and request.path not in auth_paths:
        #     return redirect(reverse('user.login'))
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
