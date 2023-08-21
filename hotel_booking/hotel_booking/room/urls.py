"""
URL mapping for room APIs

"""

from django.urls import (
    path,
)

from rest_framework.routers import DefaultRouter

from .views import BookingUpdateView, FilterRoom, PhotoViewSet, RoomListCreateView, RoomPricingDetailView, RoomPricingListView, RoomRetrieveUpdateDeleteView, RoomTypeViewSet, UserBookingView

app_name = 'room.users'

urlpatterns = [
    path('book', UserBookingView.as_view(), name='room-booking'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms-patch/<int:pk>', RoomRetrieveUpdateDeleteView.as_view(), name='room-list-patch'),
    path('room-type/', RoomTypeViewSet.as_view({'post': 'create'}), name='room-type-create'),
    path('photo/', PhotoViewSet.as_view({'post': 'create'}), name='photo-create'),
    path('booking/update/<int:booking_id>/', BookingUpdateView.as_view(), name='booking-update'),
    path('search/', FilterRoom.as_view(), name='room-search'),
    path('pricing/', RoomPricingListView.as_view(), name='room-pricing-list'),
    path('pricing/<int:pk>/', RoomPricingDetailView.as_view(), name='room-pricing-detail'),
]

