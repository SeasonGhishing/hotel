from rest_framework import viewsets
from .serializers import FacilitySerializer, HotelCreateSerializer, PhototSerializer, RatingSerializer
from .models import Hotel
from rest_framework.response import Response
from rest_framework import status

class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelCreateSerializer

    def post(self, request, format=None):
        
        serializer = HotelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Hotel is Successful Creates'}, status=status.HTTP_201_CREATED)

class FacilityViewSet(viewsets.ModelViewSet):
    serializer_class = FacilitySerializer

    def post(self, request, format=None):
        
        serializer = FacilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Facility is Successful Creates'}, status=status.HTTP_201_CREATED)

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer

    def post(self, request, format=None):
        
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Rating is Successful Creates'}, status=status.HTTP_201_CREATED)

class PhototViewSet(viewsets.ModelViewSet):
    serializer_class = PhototSerializer

    def post(self, request, format=None):
        
        serializer = PhototSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Photo is Successful Creates'}, status=status.HTTP_201_CREATED)