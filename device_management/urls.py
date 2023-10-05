from django.urls import path

from .views import DeviceListAPIview, DeviceDetailAPIView

urlpatterns = [
    path("device/", DeviceListAPIview.as_view(), name="device"),
    path("device/<int:pk>/", DeviceDetailAPIView.as_view(), name="device-detail"),
]
