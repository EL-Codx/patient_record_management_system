# app/doctors/models.py
from django.db import models
from accounts.models import User

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
