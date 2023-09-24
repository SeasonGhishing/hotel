"""
Views for the room api

"""
#from rest_framework.simplejwt.authentication import JWTAuthentication
from django.utils import timezone
from rest_framework import viewsets, mixins, status, generics, permissions, serializers
from rest_framework.permissions import IsAuthenticated

from hotel_booking.hotel.models import Hotel, HotelOwnerProfile
from hotel_booking.users.models import User
from .serializers import  BookSerializer, BookUpdateSerializer, ConformBookingSerializer, DashboardRoomPriceSerializer, DashboardRoomSerializer, DashboardSerializer, OccupancySerializer, PhotoCreateSerializers, RoomFilter, RoomSerializers, RoomPricingSerializer, RoomTypeSerializers, RoomSerializers, RoomPricingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from hotel_booking.room.models import Room, Booking, RoomPricing, RoomType
from rest_framework.generics import ListAPIView
from hotel_booking.room.confirm_booking import send_confirmation_email, send_rejection_email
from django.db.models import Sum
from drf_spectacular.utils import extend_schema, inline_serializer
from drf_spectacular.types import OpenApiTypes


class RoomPricingListView(APIView):  # Updated view name
    def get(self, request):
        room_pricings = RoomPricing.objects.all()  # Updated model reference
        serializer = RoomPricingSerializer(room_pricings, many=True)  # Updated serializer reference
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomPricingSerializer(data=request.data)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomPricingDetailView(APIView):  # Updated view name
    def get_object(self, pk):
        try:
            return RoomPricing.objects.get(pk=pk)  # Updated model reference
        except RoomPricing.DoesNotExist:  # Updated model reference
            return None

    def get(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing)  # Updated serializer reference
        return Response(serializer.data)

    def put(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing, data=request.data)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing, data=request.data, partial=True)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        room_pricing.delete()  # Updated model reference
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
Views for the room api

"""
class RoomListCreateView(generics.ListCreateAPIView):
    """Api view that handles the creation and listing of views"""
    queryset=Room.objects.all()
    serializer_class=RoomSerializers
    permission_classes=[IsAuthenticated]


class RoomRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Api view that handles the retieval, update and destroy of room object"""
    queryset=Room.objects.all()
    serializer_class=RoomSerializers
    permission_classes=[IsAuthenticated]


class RoomPricingListView(APIView):  # Updated view name
    def get(self, request):
        room_pricings = RoomPricing.objects.all()  # Updated model reference
        serializer = RoomPricingSerializer(room_pricings, many=True)  # Updated serializer reference
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomPricingSerializer(data=request.data)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomPricingDetailView(APIView):  # Updated view name
    def get_object(self, pk):
        try:
            return RoomPricing.objects.get(pk=pk)  # Updated model reference
        except RoomPricing.DoesNotExist:  # Updated model reference
            return None

    def get(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing)  # Updated serializer reference
        return Response(serializer.data)

    def put(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing, data=request.data)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing, data=request.data, partial=True)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        room_pricing.delete()  # Updated model reference
        return Response(status=status.HTTP_204_NO_CONTENT)     


class RoomTypeViewSet(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializers

    def post(self, request, format=None):
        
        serializer = RoomTypeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'RoomType is Successful Creates'}, status=status.HTTP_201_CREATED)


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoCreateSerializers

    def post(self, request, format=None):
        
        serializer = PhotoCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Photo is Successful Creates'}, status=status.HTTP_201_CREATED)


class UserBookingView(APIView):
    """

    View class of hotel booking by users.
    """

    booking_response = inline_serializer(
        name='BookingResponse',
        fields={
            'message': serializers.CharField(),
            'details': BookSerializer(),
        }
    )

    @extend_schema(
        summary="Book a hotel room",
        description="Book a hotel room as a user.",
        responses={201: booking_response},
        request=BookSerializer()
    )

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Room is successfully booked.', 'details': serializer.data}, status=status.HTTP_201_CREATED)


class BookingUpdateView(APIView):
    """

    View class of update booking for status and date change.
    """

    booking_update_response = inline_serializer(
        name='BookingUpdateResponse',
        fields={
            'start_date': serializers.DateField(),
            'end_date': serializers.DateField(),
            'status': serializers.CharField()
        }
    )

    @extend_schema(
        summary="Update booking status and dates",
        description="Update the status and dates of a booking.",
        responses={200: booking_update_response},
        request=BookUpdateSerializer(),
        parameters=[
            {
                "name": "booking_id",
                "required": True,
                "in": "path",
                "description": "ID of the booking to update",
                "schema": {"type": "integer"},
            },
        ],
    )

    def post(self, request, booking_id, format=None):
        try:
            booking = Booking.objects.get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookUpdateSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            # Update the booking's check-in, check-out dates, and status
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterRoom(generics.ListCreateAPIView):
    """

    View class for filtering room for booking.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RoomFilter
    

class BookingActionView(generics.UpdateAPIView):
    """View for accepting or rejecting the booking request"""
    queryset = Booking.objects.all()
    serializer_class = ConformBookingSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        accept_request = self.request.query_params.get('accept', '').lower() == 'true'
        
        if accept_request:
            serializer.save(status="Confirm")
            room = Room.objects.get(id=instance.room.id)
            room.room_booked += 1
            room.save()
             
            send_confirmation_email(instance.user)
        else:
            serializer.save(status="Cancel")
            send_rejection_email(instance.user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class HotelRoomViewSet(viewsets.ModelViewSet):
    serializer_class = DashboardRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="List hotel rooms",
        description="Get a list of rooms for the authenticated hotel owner.",
        responses={200: DashboardRoomSerializer(many=True)},
    )

    def get_queryset(self):
        user = self.request.user

        try:
            hotel_owner_profile = HotelOwnerProfile.objects.get(user=user)
            hotel = hotel_owner_profile.hotel

            rooms = Room.objects.filter(hotel=hotel)
            return rooms
        except HotelOwnerProfile.DoesNotExist:
            return Room.objects.none()
        
from django.utils.timezone import localdate 

today = localdate()

class SendDataToDashboard(APIView):
    """
    View class of sending data to the dashboard
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):

            user = self.request.user

            if HotelOwnerProfile.objects.get(user=user):
                hotel =  HotelOwnerProfile.hotel
                book = Booking.objects.filter(room__hotel = hotel)
                arrivals= book.objects.filter(start_date=today, status="CONFIRM").count()
                departures=book.departures()
                new_bookings=book.new_bookings()
                stay_overs=book.count_stay_overs()
                cancelled_bookings = book.cancelled_bookings()
                dashboard_data = {
                        "Arrivals":arrivals,
                        "Departures":departures,
                        "New_Bookings": new_bookings,
                        "Cancelled_Bookings":cancelled_bookings,
                        "Stay_Overs": stay_overs
                    }
                serializer = DashboardSerializer(dashboard_data)
                return Response(serializer.data, status=status.HTTP_200_OK)     
            
            if isinstance(user, User):
                is_superuser =user.is_superuser

                if is_superuser:
                
                    arrivals=Booking.arrival()
                    departures=Booking.departures()
                    new_bookings=Booking.new_bookings()
                    stay_overs=Booking.count_stay_overs()
                    cancelled_bookings = Booking.cancelled_bookings()
                    dashboard_data = {
                        "Arrivals":arrivals,
                        "Departures":departures,
                        "New_Bookings": new_bookings,
                        "Cancelled_Bookings":cancelled_bookings,
                        "Stay_Overs": stay_overs
                    }
                    serializer = DashboardSerializer(dashboard_data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message":"Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
     


class OccupancyView(APIView):
    """
    View class of Occupany data table
    """

    permission_classes = [permissions.IsAuthenticated]

    occupancy_response = inline_serializer(
        name='OccupancyResponse',
        fields={
            'occupied': serializers.IntegerField(),
            'available': serializers.IntegerField(),
            'unavailable': serializers.IntegerField(),
            'occupancy_rate': serializers.IntegerField(),
            'available_rate': serializers.IntegerField(),
            'unavailable_rate': serializers.IntegerField(),
            }
        )

    @extend_schema(
        summary="Retrieve dashboard occupancy table data",
        description="Get occupancy data for a room booking.",
        responses={200: occupancy_response},
        parameters=[
            {
                "name": "start_date",
                "required": True,
                'type': OpenApiTypes.STR,
                "description": "Start date for room booked",
                "schema": {"type": "string", "format": "date"},
            },
            {
                "name": "end_date",
                "required": True,
                'type': OpenApiTypes.STR,
                "description": "End date for room booked",
                "schema": {"type": "string", "format": "date"},
            },
        ],
    )

    def get(self, request):

        user = self.request.user

        try:
            hotel_owner_profile = HotelOwnerProfile.objects.get(user=user)
            hotel = hotel_owner_profile.hotel

            start_date = self.request.query_params.get('start_date')
            end_date = self.request.query_params.get('end_date')

            if not start_date or not end_date:
                return Response({"error": "Both start_date and end_date query parameters are required."}, status=status.HTTP_400_BAD_REQUEST)
            
            active_bookings = Booking.objects.filter(
                room__hotel=hotel,
                start_date__lte=end_date,
                end_date__gte=start_date,
                status="PENDING" 
            )
            unavailable__bookings = Booking.objects.filter(
                room__hotel=hotel,
                start_date__lte=end_date,
                end_date__gte=start_date,
                status="CONFIRM" 
            )
            
            total_rooms = Room.objects.filter(hotel=hotel).aggregate(Sum('total_rooms'))['total_rooms__sum']
            booked_rooms = active_bookings.count()
            unavailable_rooms = unavailable__bookings.count()

            available_rooms = total_rooms - booked_rooms - unavailable_rooms

            occupancy_rate = booked_rooms / total_rooms * 100 
            available_rate = available_rooms / total_rooms * 100
            unavailable_rate = unavailable_rooms / total_rooms * 100
        
            occupancy_data = {
                'occupied': booked_rooms,
                'available': available_rooms,
                'unavailable': unavailable_rooms,
                'occupancy_rate': occupancy_rate,
                'available_rate': available_rate,
                'unavailable_rate': unavailable_rate
            }
            serialized_occupancy_data = OccupancySerializer(occupancy_data).data

            return Response(serialized_occupancy_data)
        
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)