from rest_framework import viewsets
from .serializers import HotelCreateSerializer
from .models import Hotel
from rest_framework.response import Response
from rest_framework import status

class HotelViewSet(viewsets.ModelViewSet):
    def post(self, request, format=None):
        serializer = HotelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({ 'msg':'Hotel is Successful Creates'}, status=status.HTTP_201_CREATED)