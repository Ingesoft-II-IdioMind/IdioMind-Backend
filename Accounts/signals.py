from django.dispatch import receiver
from djoser.signals import user_activated
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.http import JsonResponse

@receiver(user_activated)
def send_activation_email( user, **kwargs):
    subject = settings.RESEND_SUBJECT
    recipient_list = [user.email]
    from_email = settings.RESEND_SENDER
    message = f"Hello {user.first_name},\n\n"
    message += "Welcome to IdioMind! Your account has been successfully activated.\n\n"
    message += "Thank you for joining our platform. Feel free to explore all the features and functionalities.\n\n"
    message += "If you have any questions or need assistance, please don't hesitate to reach out to our support team.\n\n"
    message += "Best regards,\n"
    message += "The IdioMind Team"

    with get_connection(
        host=settings.RESEND_SMTP_HOST,
        port=settings.RESEND_SMTP_PORT,
        username=settings.RESEND_SMTP_USERNAME,
        password=settings.RESEND_API_KEY,
        use_tls=True,
    ) as connection:
        EmailMessage(
            subject=subject,
            body=message,
            to=recipient_list,
            from_email=from_email,
            connection=connection
        ).send()

    return JsonResponse({"status": "ok"})
