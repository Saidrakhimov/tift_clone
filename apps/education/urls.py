from django.urls import path
from apps.education.views import DirectorAPIView, DirectionAPIView, FacultyAPIView, FacultyDetailAPIView

urlpatterns = [
    path("director/", DirectorAPIView.as_view()),
    path("direction/", DirectionAPIView.as_view()),
    path("faculty/", FacultyAPIView.as_view()),
    path("faculties/<int:pk>/", FacultyDetailAPIView.as_view())
]
