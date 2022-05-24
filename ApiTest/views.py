from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "login.html")

def user_login(request):
    username = request.GET["username"]
    password = request.GET["password"]
    