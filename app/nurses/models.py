# app/nurses/models.py
from django.db import models
from accounts.models import User
from app.patients.models import PatientProfile

class NurseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Vitals(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    nurse = models.ForeignKey(NurseProfile, on_delete=models.SET_NULL, null=True)
    temperature = models.FloatField()
    blood_pressure = models.CharField(max_length=20)
    pulse = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)
