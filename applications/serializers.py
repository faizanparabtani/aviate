from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import transaction
from django.core import exceptions
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

from applicants.models, jobs.models, .models import *


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


# class ApplicationSerializer(serializers.ModelSerializer):
#     class  Meta:
#         model = Appli
#         fields = '__all__'