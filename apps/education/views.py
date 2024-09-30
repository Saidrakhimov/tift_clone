from django.shortcuts import render
from apps.education.models import Direction, Director, Faculty
from rest_framework import generics, response
from rest_framework.views import APIView
from apps.education.serializer import DirectorSerializer, DirectionSerializer, FacultyListSerializer, FacultyDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class DirectorAPIView(generics.ListAPIView):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class DirectionAPIView(generics.ListAPIView):
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()


class FacultyAPIView(generics.ListAPIView):
    serializer_class = FacultyListSerializer
    queryset = Faculty.objects.all()



class FacultyDetailAPIView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyDetailSerializer