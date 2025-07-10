from django.urls import path
from . import views

urlpatterns = [
    path('', views.nurses_dashboard, name='nurses_dashboard'),
    # path('login/', views.management_login, name='management_login'),
    # path('forget-password/', views.forget_admin_password, name='forget_admin_password'),
    path('nurses_assigned_patient_management/', views.nurses_patients, name='nurses_assigned_patient_management'),
    # path('roles_and_permissions/', views.roles_permissions, name='roles_and_permissions'),
    path('nurses_appointments/', views.nurses_appointments, name='nurses_appointments'),
    path('nurses_manage_schedules/', views.nurses_manage_schedules, name='nurses_manage_schedules'),
    path('nurses_patient_medication_records/', views.nurses_patient_medication_records, name='nurses_patient_medication_records'),
    # path('appointment_report/', views.appointment_report, name='appointment_report'),
    # path('patient_activities/', views.patient_activities, name='patient_activities'),   
    # path('audit_logs/', views.audit_logs, name='audit_logs'),
    # path('system_settings/', views.system_settings, name='system_settings'),
    path('nurses_profile/', views.nurses_profile, name='nurses_profile'),
    path('nurses_notifications/', views.nurses_notifications, name='nurses_notifications'),
    path('nurses_messages/', views.nurses_messages, name='nurses_messsages')
]