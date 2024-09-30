from django.urls import path
from apps.application.views import ApplicationAPIView, ApplicationStatusListAPIView


urlpatterns = [
    path("application/", ApplicationAPIView.as_view()),
    path("application-statuses", ApplicationStatusListAPIView.as_view())
]