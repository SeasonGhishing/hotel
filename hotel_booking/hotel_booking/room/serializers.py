"""
Serializers for room api
"""
from rest_framework import serializers

from  .models import Book, Photo, Room, RoomPricing, RoomType


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
    
class BookSerializer(serializers.ModelSerializer):
    """

    Description: Serializer class of booking room by user.
    """
    class Meta:
        model = Book
        fields = ('user', 'room', 'details', 'room_number', 'start_date', 'end_date', 'checkout_status')

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


"""
Serializers for room api
"""
from rest_framework import serializers

from  hotel_booking.room.models import Room, RoomPricing
room_photo = serializers.PrimaryKeyRelatedField(
        queryset=Photo.objects.all(),
        many=True,
    )


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

        
        #for photo in photo_data:
            #Photo.objects.create(room=room, **photo) 
        
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

























"""class RoomPricingSerializer(serializers.ModelSerializer):
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

        return data"""
