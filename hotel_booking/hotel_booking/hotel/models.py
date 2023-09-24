from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from hotel_booking.core.models import TimeStampAbstractModel, upload_path
from django.db import models
from django.utils.crypto import get_random_string
    
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

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    photos = models.ManyToManyField(Photo, through='HotelPhoto')
    facility = models.ManyToManyField(Facility, through='HotelFacility')
    ratings = models.ManyToManyField(Rating, through='HotelRating')

    class Meta:
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.name

class HotelOwnerProfile(TimeStampAbstractModel):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="hotel_owner"
    )
    mobile_no = PhoneNumberField()
    avatar = models.ImageField("Image", upload_to=upload_path, blank=True, null=True)
    hotel = models.OneToOneField(Hotel, related_name="hotel_name", on_delete=models.CASCADE, default=1)
    
class HotelFacility(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    date_of_added = models.DateTimeField(auto_now_add=True)

class HotelRating(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    date_of_posted = models.DateTimeField(auto_now_add=True)

class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    date_of_added = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    TRANS_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirm', 'Confirm'),
        ('check_in', 'Check In'),
        ('check_out', 'Check Out'),
        ('cancel', 'Cancel'),
    )
    
    trans_id = models.CharField(max_length=255, null=True, blank=True)
    pay_date = models.DateField()
    pay_method = models.CharField(max_length=100)
    pay_status = models.CharField(max_length=10, choices=TRANS_STATUS_CHOICES, default='pending')
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_by = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.pay_method == 'cash' and not self.trans_id:
            self.trans_id = get_random_string(length=10)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment #{self.id}: {self.pay_amount} - {self.pay_date}"
    

class Revenue(models.Model):
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_bookings = models.IntegerField()
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Revenue Data: Sales - {self.total_sales}, Bookings - {self.total_bookings}"