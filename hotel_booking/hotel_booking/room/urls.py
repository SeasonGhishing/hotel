"""
URL mapping for room APIs

"""

from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter

from .views import RoomViewSet, RoomPricingListView, RoomPricingDetailView

router = DefaultRouter()
router.register('room', RoomViewSet)

app_name = 'room'

urlpatterns = [
    path('', include(router.urls)),
    path('rooms/', RoomPricingListView.as_view(), name='room-pricing-list'),
    path('rooms/<int:pk>/', RoomPricingDetailView.as_view(), name='room-pricing-detail'),
]
