from django.contrib import admin
from apps.education.models import *


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'bio', 'phone_number', 'picture']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['title', 'bio', 'degree']


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'education_type']
