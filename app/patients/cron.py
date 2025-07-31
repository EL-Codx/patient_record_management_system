# from django_cron import CronJobBase, Schedule

# class MoveOldMedicalRecords(CronJobBase):
#     RUN_EVERY_MINS = 1440
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'patients.move_old_records'

#     def do(self):
#         from datetime import date
#         from .models import MedicalRecord, MedicalHistory  # Import inside the method
#         today = date.today()

#         old_records = MedicalRecord.objects.exclude(visit_date=today)
#         for record in old_records:
#             MedicalHistory.objects.create(
#                 patient=record.patient,
#                 past_illness=record.current_diagnosis,
#                 past_medications=record.current_medications,
#                 old_doctor_notes=record.doctor_notes,
#                 surgeries=record.surgery,
#                 allergies=record.allergies,
#                 family_histrory=record.family_histrory,
#                 medication=record.current_medications,
#                 treatment_note=record.treatment_note,
#                 symtoms=record.symtoms,
#                 vital_signs=record.vital_signs,
#                 visit_date=record.visit_date
#             )
#             record.delete()
