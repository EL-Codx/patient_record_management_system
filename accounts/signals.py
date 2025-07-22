from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User
from app.patients.models import PatientProfile
from app.doctors.models import DoctorProfile
from app.nurses.models import NurseProfile

# save signal
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'patient':
            PatientProfile.objects.create(user=instance, is_active=False,)
        elif instance.role == 'doctor':
            DoctorProfile.objects.create(user=instance, is_active=False,)
        elif instance.role == 'nurse':
            NurseProfile.objects.create(user=instance, is_active=False,)
            
        # Optionally handle admin role later


# delete signal
@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        if instance.role == 'patient':
            instance.patientprofile.delete()
        elif instance.role == 'doctor':
            instance.doctorprofile.delete()
        elif instance.role == 'nurse':
            instance.nurseprofile.delete()
    except Exception:
        pass  # Profile may not exist if not fully created
