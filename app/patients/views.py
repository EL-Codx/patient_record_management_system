from django.shortcuts import render

def patient_dashboard(request):
    return render(request, 'patient_index.html')


# appointments
def patient_appointments(request):
    return render(request, 'patient_appointment.html')


# medical records
def patient_medical_records(request):
    return render(request, 'patient_medicals.html')


# profile
def patient_profile(request):
    return render(request, 'patient_profile.html')