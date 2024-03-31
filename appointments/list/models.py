from django.db import models

class Appointments(models.Model):
    title=models.CharField(max_length=50)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=10)
