"""
Serializers for room api
"""
from rest_framework import serializers
from hotel_booking.hotel.models import Hotel
from hotel_booking.hotel.serializers import HotelCreateSerializer
from  .models import Book, Occupancy, Photo, Room, RoomPricing, RoomType
from  hotel_booking.room.models import Room, RoomPricing
from django_filters import rest_framework as filters, ModelChoiceFilter, RangeFilter
from django.utils import timezone

class RoomPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPricing
        fields = ('id', 'name', 'price_with_breakfast', 'price_without_breakfast', "adult_price",
                  'discount_percentage', 'surge_percentage')

    def validate(self, data):
        price_with_breakfast = data.get('price_with_breakfast', self.instance.price_with_breakfast if self.instance else None)
        price_without_breakfast = data.get('price_without_breakfast', self.instance.price_without_breakfast if self.instance else None)
        # price_with_breakfast = data.get('price_with_breakfast', self.instance.price_with_breakfast)
        # price_without_breakfast = data.get('price_without_breakfast', self.instance.price_without_breakfast)

        if price_with_breakfast is not None and price_with_breakfast < 0:
            raise serializers.ValidationError("Price with breakfast must be a positive value.")
        if price_without_breakfast is not None and price_without_breakfast < 0:
            raise serializers.ValidationError("Price without breakfast must be a positive value.")

        return data

"""
Serializers for room api
"""
class RoomSerializers(serializers.ModelSerializer):
    """Serializers for recipe"""

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'room_type', 
                  'description', 'occupancy_child',
                  'occupancy_adult','features', 'room_booked',
                  'total_rooms','room_photo']
    

    def create(self, validated_data):
        photo_data = validated_data.pop('room_photo')  
        room = Room.objects.create(**validated_data) 
        room.room_photo.set(photo_data)
        return room
    
    def update(self, instance, validated_data):
        """ TO update the Room"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        """TO delete room"""
        instance.delete()

class PhotoCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ("id", "order", "image")
    
    def create(self, validated_data):
        """ Create a new facility 
        from the validated data. """
        return Photo.objects.create(**validated_data)

class RoomTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ("id", "name")
    
    def create(self, validated_data):
        """ Create a new facility 
        from the validated data. """
        return RoomType.objects.create(**validated_data)

class BookSerializer(serializers.ModelSerializer):
    """

    Description: Serializer class of booking room by user.
    """
    class Meta:
        model = Book
        fields = ('user', 'room', 'details', 'room_number', 'start_date', 'end_date', 'status')

    def validate_user(self, user):
        """
        Check whether user is register or not. 
        Check whether user type is customer or not. 
        """
        if user is None:
            raise serializers.ValidationError('User is not found.')
        #if user.user_type != 'CUSTOMER':
            #raise serializers.ValidationError('You must be a customer to book a room.')
        return user
    
    def validate_date(self, data):
        """
        validate the start date of booking.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError('The start date must be before the end date.')
        return data

    def create(self, validated_data):
        """ Create a new facility 
        from the validated data. """
        return Book.objects.create(**validated_data)

class BookUpdateSerializer(serializers.ModelSerializer):
    """

    Description: This serializer is use to update the start and end date of booking with change of their status.
    """
    class Meta:
        model = Book
        fields = ['start_date', 'end_date', 'status']

class RoomFilter(filters.FilterSet):
    """

    Description: This serializer is use the django filter tools to filter the room for booking
    """
    room_booked = filters.NumberFilter(field_name='room_booked', lookup_expr='exact')
    room_type = filters.ModelChoiceFilter(queryset=RoomType.objects.all()) 
    hotel = filters.ModelChoiceFilter(queryset=Hotel.objects.all())
    hotel_name = filters.CharFilter(field_name='hotel__name', lookup_expr='exact')
    location = filters.CharFilter(field_name='hotel__location', lookup_expr='exact')
    occupancy_adult = filters.NumberFilter(field_name='occupancy_adult', lookup_expr='gte')
    occupancy_child = filters.NumberFilter(field_name='occupancy_child', lookup_expr='gte')
    #occupancy_adult = RangeFilter()

    class Meta:
        model = Room
        fields = []

#qs = Room.objects.all().order_by('hotel')
#f = RoomFilter({'occupancy_adult_min': '1'}, queryset=qs)
#f = RoomFilter({'occupancy_adult_min': '2', 'occupancy_adult_max': '5'}, queryset=qs)

class OccupancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupancy
        fields = '__all__'

class OccupancyFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='end_date', lookup_expr='lte')
    
    # today = filters.DateFilter(field_name='start_date', lookup_expr='date', method='filter_today')
    # this_month = filters.DateFilter(field_name='start_date', lookup_expr='month', method='filter_this_month')
    # this_year = filters.DateFilter(field_name='start_date', lookup_expr='year', method='filter_this_year')

    class Meta:
        model = Occupancy
        fields = ['start_date', 'end_date']

    # def filter_today(self, queryset, name, value):
    #     today = timezone.now().date()
    #     return queryset.filter(start_date=today)

    # def filter_this_month(self, queryset, name, value):
    #     if value:
    #         this_month = timezone.now().month
    #         this_year = timezone.now().year
    #         return queryset.filter(start_date__month=this_month, start_date__year=this_year)
    #     return queryset

    # def filter_this_year(self, queryset, name, value):
    #     this_year = timezone.now().year
    #     return queryset.filter(start_date__year=this_year)


class ConformBookingSerializer(serializers.ModelSerializer):
    """Serializer class for confirmation of the booking process"""

    class Meta:
        model = Book
        fields = ('user', 'status')  



















class DashboardRoomtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['name']

class DashboardPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
    
class DashboardHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name']

class DashboardRoomPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPricing
        fields = '__all__'

class DashboardRoomSerializer(serializers.ModelSerializer):
    room_type = DashboardRoomtypeSerializer(read_only=True)
    hotel = DashboardHotelSerializer(read_only=True)
    price = DashboardRoomPriceSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'room_type', 'room_photo', 'hotel', 'occupancy_adult', 'occupancy_child', 'total_rooms', 'price']


class DashboardSerializer(serializers.Serializer):
    Arrivals = serializers.IntegerField()
    Departures = serializers.IntegerField()
    New_Bookings = serializers.IntegerField()
    Cancelled_Bookings = serializers.IntegerField()
    Stay_Overs = serializers.IntegerField()