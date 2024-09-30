from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import NewsContent
from datetime import datetime


class NewsContentApiTestCase(APITestCase):
    def set_up(self):
        self.item = NewsContent.objects.create(
            title="News title",
            body="test news body",
            is_published=True,
            published_time=datetime(2024, 9, 11, 12, 30, 30),
            name="Test Item", description="Test description"
        )
        self.list_url = reverse('news-list')

    def test_news_content_list_api(self):
        response = self.client.get(self.list_url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


__all__ = ['NewsContentApiTestCase']
