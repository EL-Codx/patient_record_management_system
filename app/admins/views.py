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


# management dashboard
def patient_management_view(request):
    return render(request, 'patient_mgt_view.html', {})