from django.db.models import Count
from django.shortcuts import render
from . serializers import (
    ApplicationListSerializer,
)
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import permissions
import json

from . models import *
from applicants.models import User


class ApplicationListView(APIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        applications = Application.objects.all()
        serializer = ApplicationListSerializer(snippets, many=True)
        return Response(serializer.data)



class ApplicationView(APIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, applicant, job, format=None):
        if applicant == None and job != None:
            try:
                applications = Application.objects.filter(job=job)
                data = ApplicationSerializer(test_record, many=True).data
            return Response(data, status=status.HTTP_200_OK)
                return Application.objects.filter(job=job)
            except Application.DoesNotExist:
                raise Http404
            
