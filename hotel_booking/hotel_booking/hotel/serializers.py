from rest_framework import serializers
from .models import Facility, Hotel, Photo, Rating

class HotelCreateSerializer(serializers.ModelSerializer):
    facility = serializers.PrimaryKeyRelatedField(
        queryset=Facility.objects.all(),
        many=True,
    )
    ratings = serializers.PrimaryKeyRelatedField(
        queryset=Rating.objects.all(),
        many=True,
    )
    photos = serializers.PrimaryKeyRelatedField(
        queryset=Photo.objects.all(),
        many=True,
    )
    
    class Meta:
        model = Hotel
        fields = (
            "id",
            "name",
            "location",
            "photos",
            "facility",
            "ratings",
        )

    def create(self, validated_data):
        """ Create a new hotel 
        from the validated data. """
        facility_data = validated_data.pop('facility')
        rating_data = validated_data.pop('ratings')
        photo_data = validated_data.pop('photos')
        
        hotel =  Hotel.objects.create(**validated_data)
        hotel.facility.set(facility_data)
        hotel.ratings.set(rating_data)
        hotel.photos.set(photo_data)

        return hotel
        

    
class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = ("id", "name", "type", "description")
    
    def create(self, validated_data):
        """ Create a new facility 
        from the validated data. """
        return Facility.objects.create(**validated_data)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ("id", "description", "star")
    
    def create(self, validated_data):
        """ Create a new rating 
        from the validated data. """
        return Rating.objects.create(**validated_data)

class PhototSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ("id", "image")
    
    def create(self, validated_data):
        """ Create a new photo 
        from the validated data. """
        return Photo.objects.create(**validated_data)
