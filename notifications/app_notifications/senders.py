# coding=utf-8
from django.conf import settings
from django.core import mail
from django.core.mail import EmailMessage

from app_notifications.base import SenderBase


class SMTPSender(SenderBase):
    @staticmethod
    def _create_email_messages(messages):
        email_messages = []
        for message in messages:
            email_message = EmailMessage(
                subject=message['subject'],
                body=message['content'],
                from_email=settings.FROM_EMAIL,
                to=[message['email']]
            )
            email_message.content_subtype = 'html'
            email_messages.append(email_message)
        return email_messages

    @classmethod
    def send_many(cls, messages):
        connection = mail.get_connection()
        email_messages = cls._create_email_messages(messages)

        try:
            send_count = connection.send_messages(email_messages)
        except:
            raise
        else:
            return send_count
