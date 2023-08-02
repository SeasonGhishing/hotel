from django.urls import include, path
from .views import HotelViewSet


urlpatterns = [
    path('create/', HotelViewSet.as_view({'post': 'create'}), name='create'),
]