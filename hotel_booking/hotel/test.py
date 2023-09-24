from django.test import TestCase
from .models import Hotel, Facility, Rating

#Testing for hotel model
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

import pytest
from django.utils.crypto import get_random_string
from .models import Payment

@pytest.fixture
def cash_payment():
    return Payment.objects.create(
        pay_date='2023-08-15 14:00:00',
        pay_method='cash',
        pay_status='pending',
        pay_amount=100.00,
        pay_by='John Doe'
    )

@pytest.fixture
def online_payment():
    return Payment.objects.create(
        pay_date='2023-08-16 10:00:00',
        pay_method='online',
        pay_status='confirm',
        pay_amount=150.00,
        pay_by='Jane Smith'
    )

@pytest.mark.django_db
def test_trans_id_generated_for_cash_payment(cash_payment):
    assert cash_payment.trans_id

@pytest.mark.django_db
def test_trans_id_sample_for_online_payment(online_payment):
    assert online_payment.trans_id == "SAMPLE_ONLINE_TRANS_ID"
