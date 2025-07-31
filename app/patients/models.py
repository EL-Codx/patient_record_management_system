# app/patients/models.py
from django.db import models
from accounts.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=20, blank=True)
    home_address = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    photo = models.ImageField(upload_to='patients/photos/', null=True, blank=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    current_diagnosis = models.TextField()
    symptoms = models.TextField()
    vital_signs = models.TextField()
    current_medications = models.TextField()
    treatment_note = models.TextField()
    doctor_notes = models.TextField()
    surgical_state = models.BooleanField(default=False)
    surgery = models.TextField()
    allergies = models.TextField()
    family_history = models.TextField()
    visit_date = models.DateField(auto_now_add=True)

class MedicalHistory(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    past_illness = models.TextField()
    past_medications = models.TextField()
    old_doctor_notes = models.TextField()
    surgeries = models.TextField()
    allergies = models.TextField()
    family_history = models.TextField()
    medication = models.TextField()
    treatment_note = models.TextField()
    symptoms = models.TextField()
    vital_signs = models.TextField()
    visited_date = models.DateField()
    archived_date = models.DateTimeField(auto_now_add=True)


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
