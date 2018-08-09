from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# @staff_member_required #如果用户已登录，是一个staff member（User.is_staff=True），并且处于活动状态（User.is_active=True），则正常执行该视图。
from product.models.product_models import (Product, Product_description,
                                           Manufacturer, Product_attribute_value,
                                           Product_discount, Product_filter,
                                           Product_image, Product_option,
                                           Product_related, Product_Special,
                                           Product_category, Product_download)

# Create your views here.
def product(request, product_id):
    OPTION_COUNT = {}
    OPTIONS = {}
    product = Product.objects.get(product_id=product_id)
    manufacturer = Manufacturer.objects.get(id=product_id)
    attribute = Product_attribute_value.objects.get(product_id=product_id)
    description = Product_description.objects.get(product_id=product_id)
    discount = Product_discount.objects.get(product_id=product_id)
    filter = Product_filter.objects.get(product_id=product_id)
    image = Product_image.objects.filter(product__product_id=product_id)
    option = Product_option.objects.filter(product__product_id=product_id)
    for op in option:
        name_temp = op.option_value.name
        if OPTION_COUNT.get(name_temp):
            OPTION_COUNT[name_temp].append([op.name, op.image, op.quantity, op.subtract, op.price, op.integral])
        else:
            OPTION_COUNT[name_temp] = [[op.name, op.image, op.quantity, op.subtract, op.price, op.integral]]
    OPTIONS["options"]= OPTION_COUNT

    related = Product_related.objects.filter(product__product_id=product_id)
    special = Product_Special.objects.get(product_id=product_id)
    category = Product_category.objects.get(product_id=product_id)
    download = Product_download.objects.filter(product__product_id=product_id)

    content = {"product": product, "manufacturer": manufacturer,
               "attribute": attribute, "description": description,
               "discount": discount, "filter": filter,
               "image": image, "option": option,
               "related": related, "special": special,
               "category": category, "download": download}
    content.update(OPTIONS)
    print(content)
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