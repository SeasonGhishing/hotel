"""
Views for the room api

"""
#from rest_framework.simplejwt.authentication import JWTAuthentication
from django.utils import timezone
from rest_framework import viewsets, mixins, status, generics
from rest_framework.permissions import IsAuthenticated

from hotel_booking.hotel.models import Hotel, HotelOwnerProfile
from hotel_booking.users.models import User
from .serializers import  BookSerializer, BookUpdateSerializer, ConformBookingSerializer, DashboardRoomPriceSerializer, DashboardRoomSerializer, DashboardSerializer, OccupancyFilter, OccupancySerializer, PhotoCreateSerializers, RoomFilter, RoomSerializers, RoomPricingSerializer, RoomTypeSerializers, RoomSerializers, RoomPricingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from hotel_booking.room.models import Occupancy, Room, Book, RoomPricing, RoomType
from rest_framework.generics import ListAPIView

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
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Room is successfully booked.', 'details': serializer.data}, status=status.HTTP_201_CREATED)

class BookingUpdateView(APIView):
    """

    View class of update booking for status and date change.
    """
    def post(self, request, booking_id, format=None):
        try:
            booking = Book.objects.get(pk=booking_id)
        except Book.DoesNotExist:
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

from django.db.models import Q

class OccupancyFilterView(ListAPIView):
    serializer_class = OccupancySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OccupancyFilter

    def get_queryset(self):
        queryset = Occupancy.objects.all()
        now = timezone.now().date()
        this_month = now.month
        this_year = now.year

        # Check if the 'this_month' query parameter is present and set to 'true'
        if self.request.query_params.get('this_month') == 'true':
            queryset = queryset.filter(
                Q(start_date__month=this_month, start_date__year=this_year) |
                Q(end_date__month=this_month, end_date__year=this_year)
            )
        # Check if the 'today' query parameter is present and set to 'true'
        if self.request.query_params.get('today') == 'true':
            queryset = queryset.filter(
                Q(start_date__exact=now) |
                Q(end_date__exact=now)
            )

        # Check if the 'this_year' query parameter is present and set to 'true'
        if self.request.query_params.get('this_year') == 'true':
            queryset = queryset.filter(
                Q(start_date__year=this_year) |
                Q(end_date__year=this_year)
            )

        return queryset
    
from hotel_booking.room.confirm_booking import send_confirmation_email, send_rejection_email

class BookingActionView(generics.UpdateAPIView):
    """View for accepting or rejecting the booking request"""
    queryset = Book.objects.all()
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
    













class HotelViewSet(viewsets.ReadOnlyModelViewSet):
   
    serializer_class = DashboardRoomSerializer
    queryset = Room.objects.all()


class SendDataToDashboard(APIView):
    """
    View class of sending data to the dashboard
    """
    authentication_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = request.User
            if isinstance(user, User):
                is_superuser =user.is_superuser

                if is_superuser:
                
                    arrivals=Book.arrival()
                    departures=Book.departures()
                    new_bookings=Book.new_bookings()
                    stay_overs=Book.count_stay_overs()
                    cancelled_bookings = Book.cancelled_bookings()
                    dashboard_data = {
                        "Arrivals":arrivals,
                        "Departures":departures,
                        "New_Bookings": new_bookings,
                        "Cancelled_Booking":cancelled_bookings,
                        "Stay_Overs": stay_overs
                    }
                    serializer = DashboardSerializer(dashboard_data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message":"Unauthorized"}, status=status.HTTP_403_FORBIDDEN)



            if isinstance(User,HotelOwnerProfile):
                hotel =  HotelOwnerProfile.hotel
                book = Book(hotel)
                arrivals=book.arrival()
                departures=book.departures()
                new_bookings=book.new_bookings()
                stay_overs=book.count_stay_overs()
                cancelled_bookings = book.cancelled_bookings()
                dashboard_data = {
                        "Arrivals":arrivals,
                        "Departures":departures,
                        "New_Bookings": new_bookings,
                        "Cancelled_Booking":cancelled_bookings,
                        "Stay_Overs": stay_overs
                    }
                serializer = DashboardSerializer(dashboard_data)
                return Response(serializer.data, status=status.HTTP_200_OK)     
            else:
                return Response({"message":"Unauthorized"}, status=status.HTTP_403_FORBIDDEN)       
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)