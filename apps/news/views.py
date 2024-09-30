from django.shortcuts import render
from apps.news.serializer import NewsContentListSerializer, NewsContentDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.news.models import NewsContent
from django.utils import timezone


class NewsContentListAPIView(ListAPIView):
    queryset = NewsContent.objects.filter(
        is_published=True,
        published_time__lte=timezone.now()
    ).order_by("-id")
    serializer_class = NewsContentListSerializer




class NewsContentDetailSerializerAPIView(RetrieveAPIView):
    queryset = NewsContent.objects.filter(
        is_published=True,
        published_time__lte=timezone.now()
    ).order_by("-id")
    serializer_class = NewsContentDetailSerializer
    lookup_field = "slug"
