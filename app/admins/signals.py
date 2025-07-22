from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from accounts.models import User
from .models import AuditLog

@receiver(post_save, sender=User)
def log_user_create_update(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            user=instance,
            action=f"Created user account with role '{instance.role}'"
        )
    else:
        AuditLog.objects.create(
            user=instance,
            action=f"Updated user account with role '{instance.role}'"
        )

@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    AuditLog.objects.create(
        user=None,
        action=f"Deleted user account: {instance.username}"
    )
