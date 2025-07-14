from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'action')

# @admin.register(SystemSetting)
# class SystemSettingAdmin(admin.ModelAdmin):
#     list_display = ('key', 'value')
#     search_fields = ('key',)
