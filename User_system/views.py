from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import MyUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login as login_system, logout

# Create your views here.

# Create your views here.

def register(request):
    return render(request, 'User_system/register.html')


def register_in(request):
    username = request.POST.get("email", None)
    password = request.POST.get("password", None)
    password2 = request.POST.get("passwordRepeat", None)

    try:
        MyUser.objects.get(email=username)
    except Exception as e:
        print(e)
    else:
        return render(request, "User_system/register.html", {"error_name": "用户名存在"})

    if password != password2:
        return render(request, "User_system/register.html", {"error": "密码不匹配"})

    user = MyUser()
    user.email = username
    user.set_password(password)
    user.save()

    response =  HttpResponseRedirect(reverse("user:login"))
    response.set_cookie("username",username)
    return response

def login(request):
    username = request.COOKIES.get("username")
    context = {"username": username}
    return render(request, "User_system/login.html", context)


def login_in(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)

    # user = MyUser.objects.get(email=username)# if check_password(password, user.password):#两种验证方式都可以
    user = authenticate(request, email=username, password=password)
    if user is not None:
        login_system(request, user)
        response = HttpResponseRedirect(reverse("common:home"))
        response.set_cookie("username", username)
        return response
    else:
        context = {"error": "用户或密码错误"}
        return render(request, "User_system/login.html", context)
