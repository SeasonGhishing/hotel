"""
URL mapping for room APIs

"""

from django.urls import (
    path,
)

from rest_framework.routers import DefaultRouter

from .views import BookingActionView, BookingUpdateView, FilterRoom, HotelViewSet, OccupancyFilterView, PhotoViewSet, RoomListCreateView, RoomPricingDetailView, RoomPricingListView, RoomRetrieveUpdateDeleteView, RoomTypeViewSet, SendDataToDashboard, UserBookingView

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
    path('occupancy/', OccupancyFilterView.as_view(), name='occupancy-filter'),
    path('send_booking_email/<int:pk>/',BookingActionView.as_view(), name='send-conform-rejct-email'),
    path('Room-type-catalog/',HotelViewSet.as_view({'get': 'list'}), name='room-type-catalog'),
    path('dashboard-data/',SendDataToDashboard.as_view(), name='send-to-dashboard'),
]

