from apps.news.views import NewsContentListAPIView, NewsContentDetailSerializerAPIView
from django.urls import path

urlpatterns = [
    path("news/", NewsContentListAPIView.as_view()),
    path("news/<str:slug>/",NewsContentDetailSerializerAPIView.as_view())
]
