from rest_framework import serializers
from .models import Facility, Hotel

class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'location', 'star', 'description', 'photos', 'facility', 'ratings')

    def create(self, validated_data):
        """ Create a new hotel 
        from the validated data. """
        return Hotel.objects.create_hotel(**validated_data)