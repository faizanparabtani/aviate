from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('applicants.urls')),
    path('application/', include('applications.urls')),

]
