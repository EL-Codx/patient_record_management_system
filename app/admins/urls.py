from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_dashboard, name='management_dashboard'),
    path('login/', views.management_login, name='management_login'),
    path('forget-password/', views.forget_admin_password, name='forget_admin_password'),
    
    # patients
    path('patient_management/', views.patient_management_view, name='patient_management_view'),
    path('register_patient/', views.patient_register, name='register_patient'),
    path('delete_patient/<int:user_id>/', views.delete_patient, name='delete_patient'),
    
    # users
    path('users_management_view/', views.users_management_view, name='users_management_view'),
    path('register_user', views.register_user, name='register_user'),
    path('user/<int:user_id>/', views.view_user_detail, name='view_user'),
    path('user_delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    
    path('roles_and_permissions/', views.roles_permissions, name='roles_and_permissions'),
    path('appointments/', views.appointments, name='appointments'),
    path('manage_schedules/', views.manage_schedules, name='manage_schedules'),
    path('patient_record/', views.patient_record, name='patient_record'),
    path('appointment_report/', views.appointment_report, name='appointment_report'),
    path('patient_activities/', views.patient_activities, name='patient_activities'),   
    path('audit_logs/', views.audit_logs, name='audit_logs'),
    path('system_settings/', views.system_settings, name='system_settings'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('notifications/', views.notifications, name='notifications')
]