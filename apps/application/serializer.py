from rest_framework import serializers
from apps.application.models import Application
from apps.education.serializer import DirectionSerializer
from apps.common.serializer import DistrictSerializer


class ApplicationCreateAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("first_name", "last_name", "passport", "pinf", "gender", "direction", "district")

    def create(self, validated_data):
        pass
        return super().create(validated_data)


class ApplicationDetailSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()
    district = DistrictSerializer()

    status = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = (
            "first_name", "last_name", "passport", "pinf", "gender", "birth_date", "status", "direction", "district",
            "accepted_at", "created_at")

    def get_status(self, obj):
        return obj.get_status_display()

    def get_gender(self, obj):
        return obj.get_gender_display()



