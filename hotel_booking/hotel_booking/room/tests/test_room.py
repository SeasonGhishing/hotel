"""
Test for room api
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from room.models import Room

from room.serializers import RoomSerializers


ROOM_URL =  reverse('room:room-list')

def create_room(**params):
    """Create and return a sample room """
    defaults = {

    }

    defaults.update(params)

    room = Room.objects.create(**defaults)
    return room


class PublicRoomAPITests(TestCase):
    """Test unauthenticated API requests"""

    def setUP(self):
        self.client = APIClient()
    
    def test_auth_request(self):
        """Test auth is required to call API"""
        res = self.client.get(ROOM_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateRoomAPITests(TestCase):
    """Test authenticated API requests"""
