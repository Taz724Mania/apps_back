from django.shortcuts import render
from .models import Appointments
from rest_framework import viewsets, permissions
from .serializers import AppointmentsSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointments.objects.all()
    serializer_class=AppointmentsSerializer
    permission_classes=[permissions.AllowAny]
