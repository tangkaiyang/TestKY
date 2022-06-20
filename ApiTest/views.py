from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import json


# Create your views here.

# 测试接口
def get(request):
    response = dict()
    print(request.GET)
    for key, value in request.GET.items():
        response[key] = value
    return JsonResponse(response)


def post(request):
    response = dict()
    print(request.body)
    for key, value in json.loads(request.body).items():
        response[key] = value
    return JsonResponse(response)


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

# def index(request):
#     res = dict()
#     res["username"] = request.session["user"]
#     return render(request, "index.html", res)
