import json

from django.contrib.auth.models import AnonymousUser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


class AuthenticatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if ("/favicon.ico" in request.path):
            return self.get_response(request)

        # admin
        if ('/admin' in request.path):
            return self.get_response(request)

        # rest of request
        try:
            return self.get_response(request)
        except Exception as e:
            return HttpResponse(status=403)
