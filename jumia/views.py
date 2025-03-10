from django.shortcuts import render
from django import http
from django.views import View


# Create your views here.
def home(request):
    return render(request, "templates/home.html")


class myView(View):
    def get(self, request):
        return http.HttpResponse("Welcome to Django Day 3 and 4")

    def post(self, request):
        return http.HttpResponse("Hello, World!")
