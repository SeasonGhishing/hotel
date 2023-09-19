from django.urls import include, path
from .views import FacilityViewSet, HotelOwnerProfileCreateView, HotelViewSet, PhototViewSet, RatingViewSet

app_name = 'hotel.users'


urlpatterns = [
    path('create-hotel/', HotelViewSet.as_view({'post': 'create'}), name='create-hotel'),
    path('create-facility/', FacilityViewSet.as_view({'post': 'create'}), name='create-facility'),
    path('create-rating/', RatingViewSet.as_view({'post': 'create'}), name='create-facility'),
    path('create-photo/', PhototViewSet.as_view({'post': 'create'}), name='create-facility'),
    path('hotel-owner-profiles/', HotelOwnerProfileCreateView.as_view({'post': 'create'}), name='hotel-owner-profile-create'),
]