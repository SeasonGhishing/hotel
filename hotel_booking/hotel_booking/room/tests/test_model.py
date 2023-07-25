"""
Tests for models.
"""
from django.test import TestCase
from room.models import Room, RoomType
from hotel.models import Hotel



class RoomModelTests(TestCase):
    """Tests for room model"""    

    def test_create_room(self):
        """Test creating a room is successful."""
        hotel = Hotel.objects.create()

        room_type= RoomType.objects.create()

        room = Room.objects.create(

        )

        self.assertEqual(str(room), f"{room.room_type} Room")
