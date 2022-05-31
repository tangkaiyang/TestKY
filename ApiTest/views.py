from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def login(request, message=""):
    res = dict()
    res["message"] = message
    return render(request, "login.html", res)


def login_action(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    user = auth.authenticate(username=username, password=password)
    if not user:
        return login(request, "用户名或密码错误!")
    auth.login(request, user)
    request.session["user"] = username
    return HttpResponseRedirect("/index/")


def index(request):
    res = dict()
    res["username"] = request.session["user"]
    return render(request, "index.html", res)
