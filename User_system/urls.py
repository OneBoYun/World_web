from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_in/', views.register_in, name='register_in'),
    path('login/', views.login, name='login'),
    path('login_in/', views.login_in, name='login_in'),

]