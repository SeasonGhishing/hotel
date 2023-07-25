"""
Views for the room api

"""

from rest_framework.simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from .models import Room, RoomPricing
from .serializers import  RoomSerializers, RoomPricingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class RoomViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """View foo managing the room APIs"""
    serializer_class = RoomSerializers
    queryset = Room.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     """Retrieve rooms for authenticated users."""
    #     return self.queryset.order_by('room_type')


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
