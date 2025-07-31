from django.core.management.base import BaseCommand
from django.utils.timezone import now
from app.patients.models import MedicalRecord, MedicalHistory

class Command(BaseCommand):
    help = 'Archive MedicalRecords older than today into MedicalHistory'

    def handle(self, *args, **kwargs):
        today = now().date()
        records_to_archive = MedicalRecord.objects.filter(visit_date__lt=today)

        for record in records_to_archive:
            MedicalHistory.objects.create(
                patient=record.patient,
                past_illness=record.current_diagnosis,
                past_medications=record.current_medications,
                old_doctor_notes=record.doctor_notes,
                surgeries=record.surgery,
                allergies=record.allergies,
                family_history=record.family_history,
                medication=record.current_medications,
                treatment_note=record.treatment_note,
                symptoms=record.symptoms,
                vital_signs=record.vital_signs,
                visited_date=record.visit_date
            )
            record.delete()

        self.stdout.write(
            self.style.SUCCESS(f"{records_to_archive.count()} record(s) archived.")
        )
