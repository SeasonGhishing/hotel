from django.test import TestCase
from .models import Hotel, Facility, Rating

class HotelModelTestCase(TestCase):
    def setUp(self):
        self.facility1 = Facility.objects.create(
            name='Online Booking',
            type='Service',
            description='Fast and free online booking at any time.'
        )
        self.facility2 = Facility.objects.create(
            name='Special View',
            type='Environment',
            description='Good view and clean environment'
        )
        self.rating = Rating.objects.create(
            description='Rating description',
            star=4
        )
        self.hotel = Hotel.objects.create(
            name='ABC hotel',
            location='Itahari'
        )
        self.hotel.facility.add(self.facility1, self.facility2)
        self.hotel.ratings.add(self.rating)

    def test_hotel_creation(self):
        self.assertEqual(self.hotel.name, 'ABC hotel')
        self.assertEqual(self.hotel.location, 'Itahari')
        self.assertEqual(self.hotel.facility.count(), 2)
        self.assertIn(self.facility1, self.hotel.facility.all())
        self.assertIn(self.facility2, self.hotel.facility.all())
        self.assertEqual(self.hotel.ratings.count(), 1)
        self.assertIn(self.rating, self.hotel.ratings.all())