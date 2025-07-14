from django.contrib import admin
from .models import NurseProfile, Vitals

@admin.register(NurseProfile)
class NurseProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ('user__username', 'department')

@admin.register(Vitals)
class VitalsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'nurse', 'temperature', 'blood_pressure', 'pulse', 'recorded_at')
    list_filter = ('recorded_at',)
    search_fields = ('patient__user__username',)
