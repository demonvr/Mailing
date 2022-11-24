# coding=utf-8
import datetime

from app_notifications.api import MailingApi
from app_notifications.helpers import build_messages_from_model, build_additional_tag, build_html_content
from app_notifications.models import Message
from notifications.celeryapp import app


@app.task(name="tasks.send_message")
def send_message_task():
    """Отправка сообщений"""
    date_now = datetime.datetime.now()
    messages = Message.objects.select_related(
        'mailing', 'subscribers'
    ).filter(
        status__in=[Message.CREATE],
        mailing__start_at__lte=date_now,
        mailing__end_at__gte=date_now,
    )
    list_messages = build_messages_from_model(messages)
    for message in list_messages:
        message['content'] += build_additional_tag(message['message_id'])
        message['content'] = build_html_content(message)
    sent_messages = MailingApi.send(list_messages)
    if sent_messages == len(list_messages):
        # изменение статуса сообщения на Отправлено
        for message in list_messages:
            message_model = Message.objects.get(id=message['message_id'])
            message_model.status = Message.SENT
            message_model.save(update_fields=["updated_at", "status"])
