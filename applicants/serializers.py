from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.core import exceptions
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """

    To Serializer a User object

    """
    class Meta:
        model = User
        fields = ('id', 'email')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'required': False}}


class CreateUserSerializer(serializers.ModelSerializer):
    """
    User Registration Serializer
    Handles serialization of create account(Sign Up request) to django object

    Creates and saves a User
    Fields:
    First Name
    Last Name
    Email
    password - First password entry
    password2 - Confirmation of entered password

    """
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')


    # Method to validate if both passwords entered match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # Ensures that the database transaction is atomic
    @transaction.atomic
    def create(self, validated_data):
        # User Object creation
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        # Saving Objects to Database
        user.save()
        return user


class AuthCustomTokenSerializer(serializers.Serializer):
    """

    Custom Serializer to Authenticate a User

    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Check if user sent email
            if validate_email(email):
                user_request = User.objects.get(email=email,)

                email = user_request.email

            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include email and "password"')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs