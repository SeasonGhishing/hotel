from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from hotel_booking.core.models import TimeStampAbstractModel, upload_path


class HotelOwnerProfile(TimeStampAbstractModel):

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="hotel_owner"
    )
    mobile_no = PhoneNumberField()
    avatar = VersatileImageField("Image", upload_to=upload_path, blank=True, null=True)
