from rest_framework import serializers
from apps.common.models import *


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "title")


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "title")


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ("id", "title", "social", "link")


class GenderChoicesSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=255)
    value = serializers.CharField(max_length=255)
