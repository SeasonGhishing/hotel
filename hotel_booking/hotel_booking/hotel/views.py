from rest_framework import viewsets, serializers

from hotel_booking.room.models import Booking
from .serializers import FacilitySerializer, HotelCreateSerializer, HotelOwnerProfileSerializer, PaymentSerializer, PhototSerializer, RatingSerializer, RevenueSerializer
from .models import Hotel, Payment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils.timezone import make_aware
import datetime
from hotel_booking.core import models
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


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def custom_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) # creates object with validated data.
        
        # Customize the response message
        return Response({'msg': 'Payment Successfully Created'}, status=status.HTTP_201_CREATED)


class RevenueAPIView(APIView):
    def get(self, request, format=None):
        # gets from url
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date and end_date:
            start_date = make_aware(datetime.datetime.strptime(start_date, '%Y-%m-%d'))
            end_date = make_aware(datetime.datetime.strptime(end_date, '%Y-%m-%d'))
            sales_queryset = Payment.objects.filter(
                pay_status__in=['confirm', 'check_out', 'pending'],
                pay_date__range=(start_date, end_date)
            )
            total_sales = sales_queryset.aggregate(total_sales=Sum('pay_amount'))['total_sales'] or 0
        else:
            total_sales = Payment.objects.filter(pay_status__in=['confirm', 'check_out']).aggregate(total_sales=Sum('pay_amount'))['total_sales']
        
        total_bookings = Booking.objects.count()
        
        # Calculate average order value
        average_order_value = total_sales / total_bookings if total_bookings > 0 else 0
        
        # Prepare the API response data
        response_data = {
            'total_sales': total_sales,
            'total_bookings': total_bookings,
            'average_order_value': average_order_value,
        }
        serializer = RevenueSerializer(response_data)  # Serialize the data
        
        return Response(response_data, status=status.HTTP_200_OK)