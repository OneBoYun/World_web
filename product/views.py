from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# @staff_member_required #如果用户已登录，是一个staff member（User.is_staff=True），并且处于活动状态（User.is_active=True），则正常执行该视图。
from product.models.product_models import (Product, Product_description)


# Create your views here.
def product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product_description = Product_description.objects.get(product_id=product_id)
    content = {"product": product, "description": product_description}
    return render(request, 'product/introduction.html', content)


def pay(request):
    return render(request, 'product/pay.html')


def search(request):
    return render(request, "product/search.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def shopcart(request):
    return render(request, "product/shopcart.html")


def category(request):
    return render(request, "product/category.html")


def success(request):
    return render(request, "product/success.html")