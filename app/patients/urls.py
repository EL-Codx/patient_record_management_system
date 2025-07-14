from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_dashboard, name='patients_dashboard'),
    path('appointments/', views.patient_appointments, name='patient_appointment'),
    path('medical_records/', views.patient_medical_records, name='patient_medicals'),
    path('profile/', views.patient_profile, name='patient_profile'),
]
