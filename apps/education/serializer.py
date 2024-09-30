from rest_framework import serializers
from apps.education.models import Direction, Director, Faculty


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ("id", "title", "bio", "degree", "director")


class DirectionSerializer(serializers.ModelSerializer):
    language = serializers.SerializerMethodField()
    education_type = serializers.SerializerMethodField()

    class Meta:
        model = Direction
        fields = ("id", "title", "language", "body", "education_type")

    def get_language(self, obj):
        return obj.get_language_display()

    def get_education_type(self, obj):
        return obj.get_education_type_display()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("id", "full_name", "bio", "phone_number")


class FacultyDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    direction = DirectionSerializer(many=True)
    degree = serializers.SerializerMethodField()
    new_field = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ("id", "title", "degree", "director", "direction", "new_field")

    def get_degree(self, obj):
        return obj.get_degree_display()

    def get_new_field(self, obj):
        return "Salom"
