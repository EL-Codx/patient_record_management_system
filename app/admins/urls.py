from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_dashboard, name='management_dashboard'),
    path('login/', views.management_login, name='management_login'),
    path('forget-password/', views.forget_admin_password, name='forget_admin_password'),
    path('patient_management', views.patient_management_view, name='patient_management_view'),
    path('users_management_view', views.users_management_view, name='users_management_view'),
    path('roles_and_permissions', views.roles_permissions, name='roles_and_permissions'),    
]