"""
Django Model for the room 
"""
from django.db import models
from decimal import Decimal
from hotel_booking.hotel.models import Hotel
from hotel_booking.users.models import User

class RoomType(models.Model):
    name= models.CharField(unique=True, max_length=255,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    order = models.IntegerField()
    image= models.ImageField(upload_to='room_photos/')

    def __str__(self):
        return f"Photo {self.pk}"
    
    def is_main_photo(self):
        return self.order == 1

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type= models.ForeignKey(RoomType, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    occupancy_adult= models.PositiveIntegerField()
    occupancy_child = models.PositiveIntegerField()
    features = models.TextField(blank=True)
    room_photo = models.ManyToManyField(Photo)
    total_rooms = models.PositiveIntegerField()
    room_booked = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.room_type.name} Room"

    def unbooked_rooms(self):
        return self.total_rooms-self.room_booked

    def main_photo(self):
        return self.room_photo.get(order=1)

class HotelPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

class RoomPricing(models.Model):
    name = models.OneToOneField(Room, on_delete=models.CASCADE)
    adult_price = models.DecimalField(max_digits=5, decimal_places=2)
    child_price = models.DecimalField(max_digits=5, decimal_places=2)
    price_with_breakfast = models.DecimalField(max_digits=8, decimal_places=2)
    price_without_breakfast = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    surge_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def get_total_price(self, no_of_adults, no_of_children, has_breakfast):
        total_price = self.price_with_breakfast if has_breakfast else self.price_without_breakfast
        total_price += float(self.adult_price) * no_of_adults
        total_price += float(self.child_price) * no_of_children
        return total_price

    def update_prices_with_discount_and_surge(self):
        if self.discount_percentage is not None:
            discount_amount = (Decimal(self.discount_percentage) / 100) * self.price_with_breakfast
            self.price_with_breakfast -= discount_amount
            self.price_without_breakfast -= discount_amount

        if self.surge_percentage is not None:
            surge_amount = (Decimal(self.surge_percentage) / 100) * self.price_with_breakfast
            self.price_with_breakfast += surge_amount
            self.price_without_breakfast += surge_amount

        super(RoomPricing, self).save()


class Book(models.Model):

    """For booking room of the hotel."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    details = models.FileField(upload_to='', blank=True, null=True)
    room_number = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    checkout_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('start_date',)

    def __str__(self):
        return f'Booking for {self.room_number} by {self.user}'
