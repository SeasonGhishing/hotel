from django.urls import include, path

app_name = "api_v1"

urlpatterns = [
    path("users/", include("hotel_booking.users.api.v1.urls", namespace="users")),
    path(
        "hotel/",
        include("hotel_booking.hotel.api.v1.users.urls", namespace="hotel-owner"),
    ),
]
