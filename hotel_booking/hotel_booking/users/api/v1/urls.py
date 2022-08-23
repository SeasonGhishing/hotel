from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    OTPEmailVerification,
    PasswordChangeView,
    PasswordResetConfirmView,
    PassWordResetView,
    ResendVerificaitonEmailView,
    TokenObtainPairView,
    UserRegistrationView,
)

app_name = "users"

urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("verify-otp-code/", OTPEmailVerification.as_view(), name="verify_email"),
    path("jwt/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("password-reset/", PassWordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="api_password_reset_confirm",
    ),
    path(
        "resend/verification-code/",
        ResendVerificaitonEmailView.as_view(),
        name="resend_verification_email",
    ),
    path("change-password/", PasswordChangeView.as_view(), name="change_password"),
]
