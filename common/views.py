from django.shortcuts import render
from product.models.category_models import Category
from design.models import Banner
from sales.models import Sales, Sale_type
# Create your views here.

def home(request):

    sale_id = Sale_type.objects.all()[0].id
    sale = Sales.objects.filter(st__id=sale_id)

    banners = Banner.objects.filter(mode__id="1")

    category_name = Category.objects.filter(top=True)[:10]
    username = request.COOKIES.get("username", None)
    context = {"username": username, "category_name": category_name,
               "banners": banners, "sale": sale}

    return render(request, "common/home.html", context)