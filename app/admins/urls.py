from django.urls import path
from . import views

urlpatterns = [
    path('', views.management_dashboard, name='management_dashboard'),
    path('login/', views.management_login, name='management_login'),
    path('forget-password/', views.forget_admin_password, name='forget_admin_password')
]