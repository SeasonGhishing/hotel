from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings

def send_confirmation_email(user):
    subject = "Booking Confirmed"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]
    email_template_name = "email_templates/booking_confirmation.txt"

    context = {"user": user}
    text_content = loader.render_to_string(email_template_name, context)

    try:
        email = EmailMessage(subject, text_content, from_email, to)
        email.send()
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

def send_rejection_email(user):
    subject = "Booking Rejected"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]
    email_template_name = "email_templates/booking_rejection.txt"

    context = {"user": user}
    text_content = loader.render_to_string(email_template_name, context)

    try:
        email = EmailMessage(subject, text_content, from_email, to)
        email.send()
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

