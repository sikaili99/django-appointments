from django_rest_passwordreset.signals import reset_password_token_created
from templated_email import send_templated_mail
from rest_framework.response import Response
from django.dispatch import receiver
from rest_framework import status
from smtplib import SMTPException
from django.urls import reverse
import os


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    try:
        send_templated_mail(
            template_name='user_reset_password',
            from_email=os.environ.get('DEFAULT_FROM_EMAIL'),
            recipient_list= ['sikaili99@gmail.com'],
            context = {
                'current_user': reset_password_token.user,
                'username': reset_password_token.user.username,
                'email': reset_password_token.user.email,
                'reset_password_url': "{}?token={}".format(
                    instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
                    reset_password_token.key)
            }
        )
    except SMTPException as e:
        Response({"error": "There was an error sending an email,contact admin."}, status=status.HTTP_200_OK)

    return Response({'message':f"Reset link has been sent to your email {reset_password_token.user.email}"}, status=status.HTTP_200_OK)
