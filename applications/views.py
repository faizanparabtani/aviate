from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from . serializers import (
    ApplicationCreateSerializer,
    ApplicationSerializer,
    ApplicationUpdateSerializer,
)
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework import permissions
import json
from django.http import HttpResponse

from . models import *
from applicants.models import User

class ApplicationCreateView(generics.CreateAPIView):
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
        return Response(application, status=status.HTTP_200_OK)


class ApplicationView(APIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        request_body = dict(request.data)
        try:
            applicant = request_body['applicant'][0]
        except:
            applicant = None

        try:
            job = request_body['job'][0]
        except:
            job = None
            
        if applicant != None and job != None:
            try:
                applications = Application.objects.get(job=job, applicant=applicant)
                data = ApplicationSerializer(applications).data
                return Response(data, status=status.HTTP_200_OK)
            except Application.DoesNotExist:
                raise Response({'Bad Request':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        elif applicant == None and job:
            try:
                applications = Application.objects.filter(job=job)
                data = ApplicationSerializer(applications, many=True).data
                return Response(data, status=status.HTTP_200_OK)
            except Application.DoesNotExist:
                raise Response({'Bad Request':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        elif applicant and job == None:
            try:
                applications = Application.objects.filter(applicant=applicant)
                data = ApplicationSerializer(applications, many=True).data
                return Response(data, status=status.HTTP_200_OK)
            except Application.DoesNotExist:
                raise Response({'Bad Request':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            applications = Application.objects.all()
            serializer = ApplicationSerializer(applications, many=True)
            return Response(serializer.data)
            
    

class ApplicationUpdateView(generics.UpdateAPIView,
                        generics.RetrieveAPIView,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        id = self.kwargs["pk"]
        obj = get_object_or_404(Application, id=id)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)