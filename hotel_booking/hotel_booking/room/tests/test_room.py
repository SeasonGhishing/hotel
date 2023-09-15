"""Test for room model"""
from django.test import TestCase


from hotel_booking.room.models import Room, RoomType
from hotel_booking.hotel.models import Hotel



class RoomTestApi(TestCase):
    """Tests for room """
    def test_create_room(self):
        hotel1=Hotel.objects.create(name="Vhabya", location="Biratnagar")
        """Tests for creating room"""
        room_type= RoomType.objects.create(name="Deluxe")
        room = Room.objects.create(
            room_type=room_type,
            hotel=hotel1,
            description="Example room",
            occupancy_adult=1,
            occupancy_child=2,
            total_rooms=19,
            room_booked=1
        )
        self.assertEqual(str(room),room.description)