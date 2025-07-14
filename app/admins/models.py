# app/admins/models.py
from django.db import models

class AuditLog(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class SystemSetting(models.Model):
#     key = models.CharField(max_length=100, unique=True)
#     value = models.TextField()
