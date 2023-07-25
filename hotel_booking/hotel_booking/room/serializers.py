"""
Serializers for room api
"""
from rest_framework import serializers

from  .models import Room, RoomPricing

class RoomSerializers(serializers.ModelSerializer):
    """Serializers for recipe"""

    class Meta:
        model = Room
        fields = ['hotel', 'room_type', 
                  'description', 'occupancy_child',
                  'occupancy_adult','features', 'room_booked',
                  'total_rooms', 'main_photo', 'room_photos']
    

    def create(self, validated_data):

        room = Room.objects.create(**validated_data)
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

class RoomPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPricing
        fields = ('id', 'name', 'price_with_breakfast', 'price_without_breakfast', "adult_price",
                  'discount_percentage', 'surge_percentage')

    def validate(self, data):
        price_with_breakfast = data.get('price_with_breakfast', self.instance.price_with_breakfast)
        price_without_breakfast = data.get('price_without_breakfast', self.instance.price_without_breakfast)

        if price_with_breakfast is not None and price_with_breakfast < 0:
            raise serializers.ValidationError("Price with breakfast must be a positive value.")
        if price_without_breakfast is not None and price_without_breakfast < 0:
            raise serializers.ValidationError("Price without breakfast must be a positive value.")

        return data