from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login", redirect_field_name="next")
def address(request):
    return render(request, "information/address.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def bill(request):
    return render(request, "information/bill.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def billlist(request):
    return render(request, "information/billlist.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def bindphone(request):
    return render(request, "information/bindphone.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def bonus(request):
    return render(request, "information/bonus.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def change(request):
    return render(request, "information/change.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def collection(request):
    return render(request, "information/collection.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def comment(request):
    return render(request, "information/comment.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def commentlist(request):
    return render(request, "information/commentlist.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def coupon(request):
    return render(request, "information/coupon.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def email(request):
    return render(request, "information/email.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def foot(request):
    return render(request, "information/foot.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def idcard(request):
    return render(request, "information/idcard.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def index(request):
    return render(request, "information/index.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def information(request):
    return render(request, "information/information.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def logistics(request):
    return render(request, "information/logistics.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def news(request):
    return render(request, "information/news.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def order(request):
    return render(request, "information/order.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def orderlist(request):
    return render(request, "information/orderinfo.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def password(request):
    return render(request, "information/password.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def question(request):
    return render(request, "information/question.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def record(request):
    return render(request, "information/record.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def refund(request):
    return render(request, "information/refund.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def safety(request):
    return render(request, "information/safety.html")


@login_required(login_url="/user/login", redirect_field_name="next")
def setpay(request):
    return render(request, "information/setpay.html")