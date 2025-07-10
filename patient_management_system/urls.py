from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('management/', include('app.admins.urls')),
    path('account/', include('accounts.urls')),
    path('doctors/', include('app.doctors.urls')),
    path('nurses/', include('app.nurses.urls')),
]
