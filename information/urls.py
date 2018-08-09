from django.urls import path
from . import views

app_name = "information"
urlpatterns = [
    path('address/', views.address, name="address"),
    path('bill/', views.bill, name="bill"),
    path('billlist/', views.billlist, name="billlist"),
    path('bindphone/', views.bindphone, name="bindphone"),
    path('bonus/', views.bonus, name="bonus"),
    path('change/', views.change, name="change"),
    path('collection/', views.collection, name="collection"),
    path('comment/', views.comment, name="comment"),
    path('commentlist/', views.commentlist, name="commentlist"),
    path('coupon/', views.coupon, name="coupon"),
    path('email/', views.email, name="email"),
    path('foot/', views.foot, name="foot"),
    path('idcard/', views.idcard, name="idcard"),
    path('index/', views.index, name="index"),
    path('information/', views.information, name="information"),
    path('logistics/', views.logistics, name="logistics"),
    path('news/', views.news, name="news"),
    path('order/', views.order, name="order"),
    path('orderlist/', views.orderlist, name="orderlist"),
    path('password/', views.password, name="password"),
    path('question/', views.question, name="question"),
    path('record/', views.record, name="record"),
    path('refund/', views.refund, name="refund"),
    path('safety/', views.safety, name="safety"),
    path('setpay/', views.setpay, name="setpay"),
]