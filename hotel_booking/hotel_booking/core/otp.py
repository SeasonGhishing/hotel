import base64

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from pyotp import TOTP

OTP_VALIDITY_TIME: int = 60 * 15


def get_base32_key(user) -> str:
    # Generates a base32 value based on the key provided.
    # Key used should be hashed value of password.
    key = settings.SECRET_KEY + str(user.pk)
    key = bytes(key, encoding="UTF-8")
    val = base64.b32encode(key)
    val = str(val)
    return val.split("'")[1]


def generate_otp(user, digits=4) -> int:
    base32_key = get_base32_key(user)
    otp = TOTP(base32_key, interval=OTP_VALIDITY_TIME, digits=digits).now()
    return otp


def validate_otp(user, otp: int, digits=4) -> bool:
    base32_key = get_base32_key(user)
    return TOTP(base32_key, interval=OTP_VALIDITY_TIME, digits=digits).verify(otp)


def send_email_verification_code(request, user):
    otp_code = generate_otp(user)
    subject = f"Email Verification Code: {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]
    email_template_name = "email_templates/registration_code.txt"
    html_email_template_name = "email_templates/registration_code.html"
    current_site = get_current_site(request)
    site_name = current_site.name
    context = {"otp": otp_code, "site_name": site_name}
    text_content = loader.render_to_string(email_template_name, context)
    html_content = loader.render_to_string(html_email_template_name, context)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
