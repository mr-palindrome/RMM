from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Devices
from .serializers import DevicesSerializer

# Create your views here.


class DeviceListAPIview(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    permission_classes = (IsAuthenticated,)


class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    permission_classes = (IsAuthenticated,)
