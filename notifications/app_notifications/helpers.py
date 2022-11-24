# coding=utf-8
import random
import string

from django.conf import settings
from django.template import Context, Template
from django.urls import reverse


def build_html_content(message):
    """Создание html текста"""
    context = Context({
        'first_name': message['first_name'],
        'last_name': message['last_name'],
        'birthday': message['birthday']
    })

    template = Template(message['content'])
    return template.render(context)


def build_messages_from_model(messages):
    """Формирование списка словарей из модели"""
    messages_list = []
    for message in messages:
        messages_list.append(dict(
            message_id=message.id.hex,
            email=message.subscribers.email,
            first_name=message.subscribers.first_name,
            last_name=message.subscribers.last_name,
            birthday=message.subscribers.birthday,
            subject=message.mailing.subject,
            content=message.mailing.template.content
        ))
    return messages_list


def build_additional_tag(message_id):
    """Добавление тега с изображением.
    Путь до изображения состоит: hex(uuid) + случайная строка длиной от 5 до 20 симоволов,
    состоящая из цифр и букв
    """
    random_str = ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(random.randint(5, 20))
    )
    footer = '<footer><img src="{url}{path}{add_text}"></footer>'.format(
        url=settings.SITE_URL,
        path=reverse("image_output"),
        add_text=message_id + random_str
    )
    return footer
