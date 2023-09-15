"""Tests for room api"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from hotel_booking.room.models import Room, RoomType
from hotel_booking.hotel.models import Hotel

from hotel_booking.room.api.v1.users.serializers import RoomSerializers, RoomPricingSerializer

ROOM_URL = '/api/v1/room/rooms/'
# ROOM_URL = reverse('room-list-create')

def create_room_type():
    defaults = {
        'name':'Example'
    }
    room = Room.objects.create(defaults)
    return room

def create_hotel():
    defaults = {
        'name':'Example Hotle',
        'location': 'biratnaagr'
    }

def create_room(**params):
    defaults = {
            'room_type': create_room,
            'hotel':create_hotel,
            'description':"Example room",
            'occupancy_adult':1,
            'occupancy_child':2,
            'total_rooms':19,
            'room_booked':1
    }

def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)

class PublicRoomAPiTests(TestCase):
    """Test unauthenticated API requests"""
    def setUp(self):
        self.client=APIClient()
    
    def test_authRequired(self):
        """Test auth is required to call API."""
        res = self.client.get(ROOM_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRoomApiTest(TestCase):
    """Test authenticated API requests"""
    
    def setUp(self):
        self.client=APIClient
        self.user = create_user(
            email='user@example.com',
            password='test123@'
        )
        self.client.force_authenticate(self.user)
    
    def test_retreive_rooms(self):
        """Test retreiveing a list of rooms"""
        create_room()
        create_room()

        res = self.client.get(ROOM_URL)

        rooms = Room.objects.all().order_by('-id')
        serializer = RoomSerializers(rooms, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    

