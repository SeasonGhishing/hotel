from django.shortcuts import get_object_or_404
from rest_framework import generics, views
from rest_framework.response import Response

from hotel_booking.hotel.api.v1.users.serializers import HotelOwnerProfileSerializer
from hotel_booking.hotel.models import HotelOwnerProfile
from hotel_booking.hotel.permissions import IsHotelOwner


class HotelOwnerProfileAPIView(views.APIView):

    serializer_class = HotelOwnerProfileSerializer
    permission_classes = [IsHotelOwner]

    def get(self, request):

        user = request.user
        hotel_owner = get_object_or_404(HotelOwnerProfile, user=user)
        serializer = self.serializer_class(hotel_owner, read_only=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)


class HotelOwnerProfileUpdateView(generics.UpdateAPIView):

    serializer_class = HotelOwnerProfileSerializer
    permission_classes = [IsHotelOwner]
    http_method_names = ["options", "patch"]
