import datetime
from rest_framework import viewsets
from hotel_booking.core import models
from .serializers import FacilitySerializer, HotelCreateSerializer, PhototSerializer, RatingSerializer, PaymentSerializer, RevenueSerializer
from .models import Hotel, Payment
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import make_aware
from rest_framework.views import APIView
from room.models import Book

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
                pay_status__in=['confirm', 'check_out'],
                pay_date__range=(start_date, end_date)
            )
            total_sales = sales_queryset.aggregate(total_sales=models.Sum('pay_amount'))['total_sales']
        else:
            total_sales = Payment.objects.filter(pay_status__in=['confirm', 'check_out']).aggregate(total_sales=models.Sum('pay_amount'))['total_sales']
        
        total_bookings = Book.objects.count()
        
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
