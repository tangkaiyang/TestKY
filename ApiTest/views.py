from django.contrib import auth
from django.shortcuts import render


# Create your views here.

def login(request, message):
    return render(request, "login.html", message)


def login_action(request):
    res = {}
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    if not user:
        res["message"] = "用户名或密码错误"
    return render(request, "index.html")