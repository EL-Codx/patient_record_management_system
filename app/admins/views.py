from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User    
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from app.patients.models import PatientProfile
from django.db import transaction



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
    users = User.objects.filter(role='patient', is_superuser=False)
    return render(request, 'patient_mgt_view.html', {"users": users})


# user management
def users_management_view(request):
    users = User.objects.exclude(is_superuser=True).exclude(role='patient')
    return render(request, 'users.html', {'users': users})


# user registration
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        phone = request.POST.get('phone').strip()
        role = request.POST.get('role')
        username = request.POST.get('username').strip()
        notes = request.POST.get('notes').strip()

        try:
            # password
            phone_digits = ''.join(filter(str.isdigit, phone))[-4:]  # Last 4 digits
            raw_password = f"{first_name[0].lower()}{last_name[-1].upper()}{phone_digits}" 
            
            print(raw_password)

            # Create user
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                role=role,
                username=username,
                password=make_password(raw_password),
                notes=notes
            )
            
            user.save()

            messages.success(request, f"User created successfully! Password: {raw_password}")
            return redirect('users_management_view')  # or wherever your user list is

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    return redirect('users_management_view')


# single user details
def view_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})


# user edit
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.role = request.POST.get('role')
        user.notes = request.POST.get('notes')
        user.save()
        return redirect('users_management_view')  # Change to your actual list view name

    return render(request, 'edit_user.html', {'user': user})


# single user deletion
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id) # getting user
    user.delete()
    return redirect('users_management_view')


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


# register patient 
def patient_register(request):
    if request.method == 'POST':
        national_id = request.POST.get('national_id')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        
        # system generations
        # password
        phone_digits = ''.join(filter(str.isdigit, phone))[-4:]  # Last 4 digits
        raw_password = f"{first_name[0].lower()}{last_name[-1].upper()}{phone_digits}"
        
        print(raw_password)
        role = "patient" # role
        
        # Patient-specific fields
        date_of_birth = request.POST.get('date_of_birth')
        emergency_contact = request.POST.get('emergency_contact')
        home_address = request.POST.get('home_address')
        allergies = request.POST.get('allergies')
        notes = request.POST.get('notes')
        photo = request.FILES.get('photo')

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=national_id,
                    email=email,
                    password=make_password(raw_password),
                    first_name=first_name,
                    last_name=last_name,
                    role=role,
                    gender=gender
                )

                # Checking for profile existence 
                if User.objects.filter(username=national_id).exists():
                    messages.error(request, "A patient profile for this user already exists.")
                    return redirect('patient_management_view')
    
                PatientProfile.objects.create(
                    user=user,
                    date_of_birth=date_of_birth,
                    national_id=national_id,
                    emergency_contact=emergency_contact,
                    home_address=home_address,
                    allergies=allergies,
                    notes=notes,
                    photo=photo
                )

                messages.success(request, "Registration successful! Please log in.")
                return redirect('patient_management_view')

        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")

    return render(request, 'patient_mgt_view.html')


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