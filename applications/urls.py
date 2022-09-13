from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .views import *

urlpatterns = [
    path('list/', ApplicationView.as_view(), name='application_list'),
    path('create/', ApplicationCreateView.as_view(), name='create_application'),
    path('update/<int:pk>', ApplicationUpdateView.as_view(), name='update_application'),
]
