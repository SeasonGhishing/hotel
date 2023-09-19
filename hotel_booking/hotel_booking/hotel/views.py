from rest_framework import viewsets, serializers
from .serializers import FacilitySerializer, HotelCreateSerializer, HotelOwnerProfileSerializer, PhototSerializer, RatingSerializer
from .models import Hotel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Sum
from drf_spectacular.utils import extend_schema, inline_serializer


class HotelViewSet(viewsets.ModelViewSet):
    """
    Creates hotel with all the required fields.
    """
    serializer_class = HotelCreateSerializer

    hotel_create_response = inline_serializer(
        name='HotelCreateResponse',
        fields={
            'message': serializers.CharField(),
        }
    )

    @extend_schema(
        summary="Create a hotel",
        description="Create a hotel with all the required fields.",
        responses={201: hotel_create_response},
        request=HotelCreateSerializer(),
    )

    def post(self, request, format=None):
        
        serializer = HotelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Hotel is Successful Creates'}, status=status.HTTP_201_CREATED)


class FacilityViewSet(viewsets.ModelViewSet):
    """
    Creates facility with all its description.
    """

    serializer_class = FacilitySerializer

    facility_create_response = inline_serializer(
        name='FacilityCreateResponse',
        fields={
            'message': serializers.CharField(),
        }
    )

    @extend_schema(
        summary="Create a facility",
        description="Create a facility with all its description.",
        responses={201: facility_create_response},
        request=FacilitySerializer(),
    )

    def post(self, request, format=None):
        
        serializer = FacilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Facility is Successful Creates'}, status=status.HTTP_201_CREATED)


class RatingViewSet(viewsets.ModelViewSet):
    """
    Creates rating with description and stars.
    """

    serializer_class = RatingSerializer


    rating_create_response = inline_serializer(
        name='RatingCreateResponse',
        fields={
            'message': serializers.CharField(),
        }
    )

    @extend_schema(
        summary="Create a rating",
        description="Create a rating with description and stars.",
        responses={201: rating_create_response},
        request=RatingSerializer(),
    )

    def post(self, request, format=None):
        
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Rating is Successful Creates'}, status=status.HTTP_201_CREATED)


class PhototViewSet(viewsets.ModelViewSet):
    """
    Creates photo set for required hotel.
    """

    serializer_class = PhototSerializer

    photo_create_response = inline_serializer(
        name='PhotoCreateResponse',
        fields={
            'message': serializers.CharField(),
        }
    )

    @extend_schema(
        summary="Create a photo set",
        description="Create a photo set for a required hotel.",
        responses={201: photo_create_response},
        request=PhototSerializer(),
    )
    
    def post(self, request, format=None):
        
        serializer = PhototSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Photo is Successful Creates'}, status=status.HTTP_201_CREATED)


class HotelOwnerProfileCreateView(viewsets.ModelViewSet):
    
    serializer_class = HotelOwnerProfileSerializer

    def post(self, request, format=None):
        
        serializer = HotelOwnerProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Hotel OwnerProfile is Successful Creates'}, status=status.HTTP_201_CREATED)