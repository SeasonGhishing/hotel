from django.urls import include, path
from .views import FacilityViewSet, HotelViewSet, PhototViewSet, RatingViewSet, PaymentViewSet, RevenueAPIView

app_name = 'hotel.users'


urlpatterns = [
    path('create-hotel/', HotelViewSet.as_view({'post': 'create'}), name='create-hotel'),
    path('create-facility/', FacilityViewSet.as_view({'post': 'create'}), name='create-facility'),
    path('create-rating/', RatingViewSet.as_view({'post': 'create'}), name='create-facility'),
    path('create-photo/', PhototViewSet.as_view({'post': 'create'}), name='create-facility'),
    path('create-payment/', PaymentViewSet.as_view({'post': 'create'}), name='create-payment'),
    path('revenue/', RevenueAPIView.as_view(), name='revenue'),
]