from django.shortcuts import render
from rest_framework import generics, response
from apps.common.models import *
from rest_framework.views import APIView
from apps.application.serializer import ApplicationCreateAPIViewSerializer, ApplicationDetailSerializer
from apps.application.models import Application
from rest_framework.permissions import IsAuthenticated


class ApplicationAPIView(generics.CreateAPIView):
    serializer_class = ApplicationCreateAPIViewSerializer
    queryset = Application
    permission_classes = (IsAuthenticated,)


class ApplicationStatusListAPIView(generics.ListAPIView):
    serializer_class = ApplicationDetailSerializer
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
