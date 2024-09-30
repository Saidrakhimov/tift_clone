from rest_framework import generics, response
from apps.common.models import *
from apps.common.serializer import DistrictSerializer, RegionListSerializer, SocialSerializer
from rest_framework.views import APIView


class RegionListAPIView(generics.ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()


class DistrictsByReginAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    def get_queryset(self):
        region_id = self.request.parser_context['kwargs'].get("pk", None)
        qs = super().get_queryset()
        return qs.filter(region_id=region_id)


class SocialListAPIView(generics.ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


class GenderChoicesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [
            {
                "key": "male",
                "value": "Erkak"
            },
            {
                "key": "female",
                "values": "Ayol"
            }
        ]
        return response.Response(data, status=200)
