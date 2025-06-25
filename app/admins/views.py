from django.shortcuts import render


# management login
def management_login(request):
    return render(request, 'login.html', {})


# management forget password
def forget_admin_password(request):
    return render(request, 'forget-password.html', {})


# management dashboard
def management_dashboard(request):
    return render(request, 'index.html', {})


# patient management
def patient_management_view(request):
    return render(request, 'patient_mgt_view.html', {})


# user management
def users_management_view(request):
    return render(request, 'users.html', {})


# roles and permissions
def roles_permissions(request):
    return render(request, 'roles.html', {})


# appointments
def appointments(request):
    return render(request, 'appointments.html', {})


# manage schedules
def manage_schedules(request):
    return render(request, 'manage_schedules.html', {})


# patient records
def patient_record(request):
    return render(request, 'patient_record.html', {})


# appointment report
def appointment_report(request):
    return render(request, 'appointment_report.html', {})


# patient activities
def patient_activities(request):
    return render(request, 'patient_activities.html', {})


# audit logs
def audit_logs(request):
    return render(request, 'audit_logs.html', {})


# system settings
def system_settings(request):
    return render(request, 'system_settings.html', {})


# admin profile 
def admin_profile(request):
    return render(request, 'admin_profile.html', {})


# notification 
def notifications(request):
    return render(request, 'notification.html', {})