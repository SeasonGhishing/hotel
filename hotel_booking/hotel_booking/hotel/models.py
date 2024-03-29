from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from hotel_booking.core.models import TimeStampAbstractModel, upload_path
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class HotelOwnerProfile(TimeStampAbstractModel):

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="hotel_owner"
    )
    mobile_no = PhoneNumberField()
    avatar = models.ImageField("Image", upload_to=upload_path, blank=True, null=True)

class Hotel(AbstractBaseUser):
    """
    
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    photos = models.ManyToManyField('Photo')
    facility = models.ManyToManyField('Facility', through='HotelFacility')
    ratings = models.ManyToManyField('Rating', through='HotelRating')

    class Meta:
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.name
    
class Facility(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    image = models.ImageField(upload_to='Hotels')

    class Meta:
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.image.name

class Rating(models.Model):
    description = models.CharField(max_length=255)
    star = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return self.description
    
class HotelFacility(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

class HotelRating(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)