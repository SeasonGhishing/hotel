from django.urls import include, path

from hotel_booking.hotel.api.v1.users.views import (
    HotelOwnerProfileAPIView,
    HotelOwnerProfileUpdateView,
)

app_name = "hotel.users"

urlpatterns = [
    path(
        "owner/profile/", HotelOwnerProfileAPIView.as_view(), name="hotel-owner-profile"
    ),
    path(
        "owner/profile/<int:pk>/",
        HotelOwnerProfileUpdateView.as_view(),
        name="hotel-owner-profile-update",
    ),
    path("owner/", include("hotel_booking.hotel.urls", namespace="details-hotel")),

]
