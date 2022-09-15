from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from applicants.models import User
import json
from . serializers import (
    ApplicationCreateSerializer,
    ApplicationSerializer,
    ApplicationUpdateSerializer,
)

# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ApplicationCreateView(generics.CreateAPIView):
    """
    View that facilitates creation of an application
    Note: 1 Applicant can apply to a Job Role only 1 time
    Fields:

    Applicant
    Job
    Cover Letter
    Selected

    """
    queryset = Application.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ApplicationCreateSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({'Bad Request':'You can only submit 1 application per Job Role'},
            status=status.HTTP_400_BAD_REQUEST)
        application = serializer.save()
        application = ApplicationCreateSerializer(application).data
        return Response(application, status=status.HTTP_200_OK)


class ApplicationFetchView(generics.ListAPIView, PageNumberPagination):
    """
    View that facilitates retrieval of an application
    Pagniation and Filtering are Enabled

    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    pagination_class = PageNumberPagination

    filterset_fields = ['id', 'applicant', 'job', 'selected', 'cover_letter']
    search_fields = ['id', 'applicant__email', 'job__role', 'selected', 'cover_letter']
    ordering_fields = ['id', 'applicant', 'job', 'selected', 'cover_letter']

    def get(self, request, format=None):
        applications = self.get_queryset()
        filtered_data = self.filter_queryset(applications)
        paginated_data = self.paginate_queryset(filtered_data)
        data = ApplicationSerializer(paginated_data, many=True).data
        return self.get_paginated_response(data)
            
    

class ApplicationUpdateView(generics.UpdateAPIView,
                        generics.RetrieveAPIView,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    """
    View that facilitates updation of an application
    """
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Application.objects.all()

    def get_object(self):
        id = self.kwargs["pk"]
        obj = get_object_or_404(Application, id=id)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)