from django.urls import path
from apps.common.views import RegionListAPIView, DistrictsByReginAPIView, SocialListAPIView, GenderChoicesAPIView

urlpatterns = [
    path('regions/', RegionListAPIView.as_view()),
    path("<int:pk>/districts/", DistrictsByReginAPIView.as_view()),
    path("socials/", SocialListAPIView.as_view()),
    path("genders/", GenderChoicesAPIView.as_view())

]
