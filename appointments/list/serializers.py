from .models import Appointments
from rest_framework import serializers

class AppointmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Appointments
        fields=('__all__')