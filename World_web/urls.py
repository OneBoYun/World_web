"""World_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.flatpages import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from product.admin import admin_site
from product.admin import basic_site
from product.admin import advanced_site

urlpatterns = [
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path('productadmin/', admin_site.urls),#product后台
    path('basic-admin/', basic_site.urls),
    path('advanced-admin/', advanced_site.urls),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('common.urls', namespace='common')),
    path('user/', include('User_system.urls', namespace='user')),
    path('product/', include('product.urls', namespace='product')),
    path('information/', include('information.urls', namespace='information')),
    path('blog/', include('blog.urls', namespace='blog')),

]

urlpatterns += [
    path('<path:url>', views.flatpage),
]