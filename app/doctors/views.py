from django.shortcuts import render



# management dashboard
def doctors__dashboard(request):
    return render(request, 'doctors_index.html', {})


# patient management
def my_patients(request):
    return render(request, 'doctors_assigned_patients.html', {})


# appointments
def doctors_appointments(request):
    return render(request, 'doctors_appointments.html', {})


# manage schedules
def doctors_manage_schedules(request):
    return render(request, 'doctors_manage_schedules.html', {})


# patient records
def patient_medication_records(request):
    return render(request, 'patient_medication_records.html', {})


# admin profile 
def doctors_profile(request):
    return render(request, 'doctors_profile.html', {})


# notification 
def doctors_notifications(request):
    return render(request, 'doctors_notification.html', {})