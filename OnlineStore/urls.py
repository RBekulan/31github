"""
URL configuration for OnlineStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from OnlineSale.views import *
from Car.views import CarList, CarDetail
from users.views import RegistrationAPIView, ConfirmUserAPIView, AuthorizationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductList.as_view()),
    path('api/v1/product/<int:pk>/', ProductDetail.as_view()),

    path('api/v1/cars/', CarList.as_view()),
    path('api/v1/car/<int:pk>/', CarDetail.as_view()),

    path('api/v1/users/registration/', RegistrationAPIView.as_view()),
    path('api/v1/users/confirm/', ConfirmUserAPIView.as_view()),
    path('api/v1/users/authorization/', AuthorizationAPIView.as_view()),


]
