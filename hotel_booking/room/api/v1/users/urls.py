from django.urls import include, path

app_name = "room.users"

urlpatterns = [
        path("users/", include("hotel_booking.room.urls", namespace="users-rooms")),
]