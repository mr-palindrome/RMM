from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.contrib import admin

admin.autodiscover()

app_name = "auth"

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify-token/", TokenVerifyView.as_view(), name="token_verify"),
]
