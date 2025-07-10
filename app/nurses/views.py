from django.shortcuts import render


# management dashboard
def nurses_dashboard(request):
    return render(request, 'nurses_index.html', {})


# patient management
def nurses_patients(request):
    return render(request, 'nurses_assigned_patients.html', {})


# appointments
def nurses_appointments(request):
    return render(request, 'nurses_appointments.html', {})


# manage schedules
def nurses_manage_schedules(request):
    return render(request, 'nurses_manage_schedules.html', {})


# patient records
def nurses_patient_medication_records(request):
    return render(request, 'nurses_patient_medication_records.html', {})


# admin profile 
def nurses_profile(request):
    return render(request, 'nurses_profile.html', {})


# notification 
def nurses_notifications(request):
    return render(request, 'nurses_notification.html', {})


# messages
def nurses_messages(request):
    return render(request, 'nurses_messages.html')