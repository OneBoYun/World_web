from django.urls import path
from . import views
app_name = "product"
urlpatterns = [
    path('introduction/<int:product_id>', views.product, name="product"),
    path('pay/', views.pay, name="pay"),
    path('search/', views.search, name="search"),
    path('shopcart/', views.shopcart, name="shopcart"),
    path('category/', views.category, name="category"),
    path('success/', views.success, name="success"),
]