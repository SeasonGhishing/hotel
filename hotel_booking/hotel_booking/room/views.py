"""
Views for the room api

"""
#from rest_framework.simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, mixins, status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import  BookSerializer, BookUpdateSerializer, PhotoCreateSerializers, RoomFilter, RoomSerializers, RoomPricingSerializer, RoomTypeSerializers, RoomSerializers, RoomPricingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from hotel_booking.room.models import Room, Book, RoomPricing


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