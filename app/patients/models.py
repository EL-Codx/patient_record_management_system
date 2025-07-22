# app/patients/models.py
from django.db import models
from accounts.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    history = models.TextField()
    current_condition = models.TextField()
    medications = models.TextField()
    doctor_notes = models.TextField()
    visit_date = models.DateField(auto_now_add=True)

class LabTest(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lab_tests/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.DoctorProfile', on_delete=models.SET_NULL, null=True, blank=True)
    nurse = models.ForeignKey('nurses.NurseProfile', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pending')
