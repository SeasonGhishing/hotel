import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from hotel_booking.hotel_booking.hotel.models import Hotel
from models import RoomPricing, Room, RoomType
from serializers import RoomPricingSerializer

# Define the base URL for the views
LIST_CREATE_URL = reverse('room-pricing-list')  # Assumes you've set the view name using 'name' parameter in urls.py
DETAIL_URL = reverse('room-pricing-detail', args=[1])  # Assumes you've set the view name using 'name' parameter in urls.py

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_room_pricing():
    def _create_room_pricing(hotel_object, room_type_name, adult_price, child_price, price_with_breakfast):
        # Create a new Room object and link it with RoomPricing
        room = Room.objects.create(
            hotel=hotel_object,  # Linking with an existing Hotel object
            room_type=RoomType.objects.get_or_create(name=room_type_name)[0],  # Replace 'room_type_name' with an existing RoomType name or create a new one
            description="This is a sample room description.",
            occupancy_adult=2,
            occupancy_child=1,
            total_rooms=10,
            room_booked=5,
        )

        return RoomPricing.objects.create(
            name=room,
            adult_price=adult_price,
            child_price=child_price,
            price_with_breakfast=price_with_breakfast
        )
    return _create_room_pricing


def test_room_pricing_list(api_client, create_room_pricing):
    # Create some RoomPricing instances for testing
    room_pricing1 = create_room_pricing('Standard', 100, 50, 200)
    room_pricing2 = create_room_pricing('Deluxe', 150, 75, 250)

    # Send a GET request to the view
    response = api_client.get(LIST_CREATE_URL)

    # Check the response status code and data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == RoomPricingSerializer([room_pricing1, room_pricing2], many=True).data

# Rest of the test cases remain the same...


def test_create_room_pricing(api_client, create_room_pricing):
    # Data for creating a new RoomPricing instance
    data = {
        'name': 'New Pricing',
        'adult_price': 120,
        'child_price': 60,
        'price_with_breakfast': 220,
    }

    # Call the create_room_pricing fixture and pass the required arguments
    room_type_name = 'Standard'  # Replace 'Standard' with an existing RoomType name or create a new one
    hotel_object = Hotel.objects.create(name="Example Hotel", location="New York")  # Create an existing Hotel object or use a ForeignKey to link to an existing Hotel object
    response = create_room_pricing(hotel_object, room_type_name, data['adult_price'], data['child_price'], data['price_with_breakfast'])

    # Send a POST request to create a new RoomPricing instance
    response = api_client.post(LIST_CREATE_URL, data)

    # Check the response status code and data
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == data


def test_get_room_pricing_detail(api_client, create_room_pricing):
    # Create a RoomPricing instance for testing
    room_pricing = create_room_pricing('Standard', 100, 50, 200)

    # Send a GET request to the detail view
    response = api_client.get(DETAIL_URL)

    # Check the response status code and data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == RoomPricingSerializer(room_pricing).data

def test_update_room_pricing(api_client, create_room_pricing):
    # Create a RoomPricing instance for testing
    room_pricing = create_room_pricing('Standard', 100, 50, 200)

    # Data for updating the RoomPricing instance
    updated_data = {
        'name': 'Updated Pricing',
        'adult_price': 130,
        'child_price': 65,
        'price_with_breakfast': 210,
    }

    # Send a PUT request to update the RoomPricing instance
    response = api_client.put(DETAIL_URL, updated_data)

    # Check the response status code and data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == updated_data

def test_partial_update_room_pricing(api_client, create_room_pricing):
    # Create a RoomPricing instance for testing
    room_pricing = create_room_pricing('Standard', 100, 50, 200)

    # Data for partial update of the RoomPricing instance
    partial_data = {
        'name': 'Updated Pricing',
    }

    # Send a PATCH request to partially update the RoomPricing instance
    response = api_client.patch(DETAIL_URL, partial_data)

    # Check the response status code and updated data
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == partial_data['name']

def test_delete_room_pricing(api_client, create_room_pricing):
    # Create a RoomPricing instance for testing
    room_pricing = create_room_pricing('Standard', 100, 50, 200)

    # Send a DELETE request to delete the RoomPricing instance
    response = api_client.delete(DETAIL_URL)

    # Check the response status code and verify the instance is deleted
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not RoomPricing.objects.filter(pk=room_pricing.pk).exists()
