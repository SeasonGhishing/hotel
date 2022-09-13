from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from hotel_booking.hotel.models import HotelOwnerProfile
from hotel_booking.users.models import User


class UserBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]


class HotelOwnerProfileSerializer(serializers.ModelSerializer):

    user_details = UserBasicInfoSerializer(source="user", read_only=True)
    avatar = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
        ]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].required = False

    class Meta:
        model = HotelOwnerProfile
        fields = ["id", "mobile_no", "avatar", "user_details"]
