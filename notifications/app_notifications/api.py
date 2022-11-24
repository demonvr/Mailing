# coding=utf-8
from app_notifications.senders import SMTPSender


class MailingApi():

    @staticmethod
    def change_messages_status(message, message_status):
        """Изменяет статус сообщения"""
        message.status = message_status
        message.save(update_fields=["updated_at", "status"])

    @classmethod
    def send(cls, list_messages):
        messages = []
        for message in list_messages:
            messages.append(
                dict(
                    subject=message['subject'],
                    content=message['content'],
                    email=message['email']
                )
            )
        return SMTPSender.send_many(messages)



