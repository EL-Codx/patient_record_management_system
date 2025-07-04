from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors__dashboard, name='doctors__dashboard'),
    # path('login/', views.management_login, name='management_login'),
    # path('forget-password/', views.forget_admin_password, name='forget_admin_password'),
    path('assigned_patient_management/', views.my_patients, name='assigned_patient_management'),
    # path('roles_and_permissions/', views.roles_permissions, name='roles_and_permissions'),
    path('doctors_appointments/', views.doctors_appointments, name='doctors_appointments'),
    path('doctors_manage_schedules/', views.doctors_manage_schedules, name='doctors_manage_schedules'),
    path('patient_medication_records/', views.patient_medication_records, name='patient_medication_records'),
    # path('appointment_report/', views.appointment_report, name='appointment_report'),
    # path('patient_activities/', views.patient_activities, name='patient_activities'),   
    # path('audit_logs/', views.audit_logs, name='audit_logs'),
    # path('system_settings/', views.system_settings, name='system_settings'),
    path('doctors_profile/', views.doctors_profile, name='doctors_profile'),
    path('doctors_notifications/', views.doctors_notifications, name='doctors_notifications')
]