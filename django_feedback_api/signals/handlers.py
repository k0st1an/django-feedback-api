# coding: utf-8

from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save

from django_feedback_api.models import FeedBack


@receiver(post_save, sender=FeedBack)
def send_email(instance, **kwargs):
    recipient_list = getattr(settings, 'MANAGERS')
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')

    if not recipient_list:
        return

    if not from_email or from_email == 'webmaster@localhost':
        return

    send_mail(
        subject=getattr(settings, 'FEEDBACK_SUBJECT', 'New feedback'),
        message=build_message(**instance.get_saved_data()),
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=True
    )


def build_message(**kwargs):
    message = 'Hello!\n\n'
    message += 'New feedback from {name} <{email}>'.format(**kwargs)

    if kwargs.get('phone_number'):
        message += ' (phone number: {phone_number}).\n\n'.format(**kwargs)
    else:
        message += '.\n\n'

    message += 'Text message: {message}\n\n'.format(**kwargs)
    message += '---\nInfomation:\n'
    message += '\tMessage created: {created}\n'.format(**kwargs)
    message += '\tClient IP: {ip}\n'.format(**kwargs)
    message += '\tMessage sent from: {url}\n'.format(**kwargs)

    return message
