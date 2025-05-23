"""
URL configuration for user_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user_management.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", register, name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/myinfo/", CustomerView.as_view(), name="myinfo"),
    path("api/user/<username>/", UserView.as_view()),
    path("api/address/", AddressListView.as_view(), name="address-list"),
    path("api/address/<int:pk>/", AddressDetailView.as_view(), name="address-detail"),
    path("api/address/default/", DefaultAddressView.as_view(), name="address-default"),
    path(
        "api/payment/",
        PaymentMethodListView.as_view(),
        name="paymentmethod-list",
    ),
    path(
        "api/payment/<int:pk>/",
        PaymentMethodDetailView.as_view(),
        name="paymentmethod-detail",
    ),
    path("api/change_password/", ChangePasswordView.as_view(), name="change-password"),
]
