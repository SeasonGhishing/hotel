"""
Views for the room api

"""

#from rest_framework.simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from .models import Room, RoomPricing
from .serializers import  BookSerializer, PhotoCreateSerializers, RoomSerializers, RoomPricingSerializer, RoomTypeSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from drf_spectacular.utils import extend_schema



class RoomPricingListView(APIView):  # Updated view name
    
    @extend_schema(
        description="List all room pricings.",
        responses={
            200: {"description": "List of room pricings", "schema": RoomPricingSerializer(many=True)},
        },
    )
    
    def get(self, request):
        room_pricings = RoomPricing.objects.all()  # Updated model reference
        serializer = RoomPricingSerializer(room_pricings, many=True)  # Updated serializer reference
        return Response(serializer.data)


    @extend_schema(
        description="Create a new room pricing.",
        request={"serializer": RoomPricingSerializer},
        responses={
            201: {"description": "Room pricing created successfully", "schema": RoomPricingSerializer},
            400: {"description": "Bad Request"},
        },
    )
    
    def post(self, request):
        serializer = RoomPricingSerializer(data=request.data)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomPricingDetailView(APIView):
    @extend_schema(
        description="Retrieve a room pricing by ID.",
        responses={
            200: {"description": "Room pricing details", "schema": RoomPricingSerializer},
            404: {"description": "Not Found"},
        },
    )
    def get(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing)  # Updated serializer reference
        return Response(serializer.data)
    
    @extend_schema(
        description="Update a room pricing by ID.",
        request={"serializer": RoomPricingSerializer},
        responses={
            200: {"description": "Room pricing updated successfully", "schema": RoomPricingSerializer},
            400: {"description": "Bad Request"},
            404: {"description": "Not Found"},
        },
    )

    def put(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing, data=request.data)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        description="Partially update a room pricing by ID.",
        request={"serializer": RoomPricingSerializer},
        responses={
            200: {"description": "Room pricing partially updated successfully", "schema": RoomPricingSerializer},
            400: {"description": "Bad Request"},
            404: {"description": "Not Found"},
        },
    )

    def patch(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RoomPricingSerializer(room_pricing, data=request.data, partial=True)  # Updated serializer reference
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        description="Delete a room pricing by ID.",
        responses={
            204: {"description": "Room pricing deleted successfully"},
            404: {"description": "Not Found"},
        },
    )

    def delete(self, request, pk):
        room_pricing = self.get_object(pk)  # Updated model reference
        if not room_pricing:
            return Response(status=status.HTTP_404_NOT_FOUND)
        room_pricing.delete()  # Updated model reference
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserBookingView(APIView):
    """

    View class of hotel booking by users.
    """
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Room is successfully booked.', 'details': serializer.data}, status=status.HTTP_201_CREATED)


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
