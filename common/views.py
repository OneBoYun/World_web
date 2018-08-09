from django.shortcuts import render

# Create your views here.

def home(request):
    username = request.COOKIES.get("username", None)
    context = {"username": username}
    return render(request, "common/home.html", context)