from django.contrib import admin
from .models import PatientProfile, MedicalRecord, LabTest, Appointment

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone', 'address')
    search_fields = ('user__username', 'phone')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'visit_date')
    search_fields = ('patient__user__username',)
    list_filter = ('visit_date',)

@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'uploaded_at')
    list_filter = ('uploaded_at',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'nurse', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient__user__username', 'doctor__user__username')
