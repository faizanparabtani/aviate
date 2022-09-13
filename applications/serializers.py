from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import transaction
from django.core import exceptions
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

from .models import *
from applicants.models import User
from jobs.models import Job

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        # Application Object creation
        application = Application.objects.create(
            applicant=validated_data['applicant'],
            job=validated_data['job'],
            cover_letter=validated_data['cover_letter'],
            selected=validated_data['selected'],
        )
        # Saving Objects to Database
        application.save()
        return application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('selected', 'cover_letter')

    def update(self, instance, validated_data):
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance