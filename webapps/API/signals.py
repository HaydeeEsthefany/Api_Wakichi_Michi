from django.core.mail import EmailMultiAlternatives #send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string
from web.settings import BACK_END_URL, CDN_URL, EMAIL_HOST_USER

from rest_framework_jwt.settings import api_settings


def send_email_token_bbva(  token ,email, *args, **kwargs):
    context = {
        'cdn_url' : CDN_URL,
        'reset_password_url': "{}{}".format(BACK_END_URL, token)
    }

    # render email text
    email_html_message = render_to_string('email-recovery-password.html', context)
    msg = EmailMultiAlternatives(
        # title:
        "VALIDAR IDENTIDAD - BBVA",
        # message:
        "",
        # from:
        EMAIL_HOST_USER,
        # to:
        [email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()