from django.test import TestCase
from django.contrib.auth import get_user_model
from hotel_booking.hotel.models import Hotel
from hotel_booking.room.models import Book, Room, RoomType, Photo
from hotel_booking.hotel.models import Hotel
from rest_framework.test import APIClient


class CustomUserManagerTestCase(TestCase):
    def test_create_user(self):
        User = get_user_model()
        email = "testuser@example.com"
        password = "testpassword"

        # Create a regular user
        user = User.objects.create_user(email=email, password=password)
        self.assertIsNotNone(user)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, email)
        self.assertFalse(user.email_verified)

class RoomAPITest(TestCase):
    def setUp(self):
        self.client=APIClient()

        # Create a RoomType for testing
        self.room_type = RoomType.objects.create(name='Test Room Type')
        
        # Create a Hotel for testing
        self.hotel = Hotel.objects.create(name='Test Hotel')
        
        # Create a Photo for testing
        self.photo = Photo.objects.create(order=1, image='path/test_image.jpg')
        
        # Create a Room for testing
        self.room_data = {
            'hotel': self.hotel,
            'room_type': self.room_type,
            'description': 'Test Room Description',
            'occupancy_adult': 2,
            'occupancy_child': 1,
            'features': 'Test Room Features',
            'room_booked': 5,
            'total_rooms': 10,
        }

    def test_book_room(self):
        # Create a user
        self.client=APIClient()


        self.user = get_user_model()
        user = self.user.objects.create_user(email="testuser@example.com", password="testpassword")
        self.client.force_authenticate(self.user)

        # Create a room to be booked
        room = Room.objects.create(**self.room_data)

        # Book the room for the user
        booking_data = {
            'user': user.id,
            'room': room.id,
            'room_number': '101', 
            'start_date': '2023-08-10',
            'end_date': '2023-08-15',
            'checkout_status': False,  
        }

        url = 'http://127.0.0.1:8000/api/v1/rooms/users/book'
        response = self.client.post(url, booking_data)  

        self.assertEqual(response.status_code, 201)
        #booking = Book.objects.filter(user=user, room=room).first()
        #self.assertIsNotNone(booking)
        #self.assertEqual(booking.room_number, '101')
        #self.assertEqual(booking.start_date, '2023-08-10')
        #self.assertEqual(booking.end_date, '2023-08-15')
