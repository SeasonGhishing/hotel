from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField, EmailField
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    """Default user for Hotel Booking."""

    SOCIAL_AUTH_PROVIDERS = (
        ("GOOGLE", ("GOOGLE")),
        ("FACEBOOK", ("FACEBOOK")),
        ("TWITTER", ("TWITTER")),
        ("APPLE", ("APPLE")),
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(_("Email Address"), unique=True)
    email_verified = BooleanField(default=False)
    social_auth = CharField(
        choices=SOCIAL_AUTH_PROVIDERS,
        max_length=100,
        blank=True,
        null=True,
        help_text="This field indicates through which social app has user logged in or signup",
    )
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name or self.email or self.mobile or ""
