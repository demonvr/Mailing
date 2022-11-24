# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models


from sdk.models import TimeStampedModelMixin, UUIDModel


class Subscribers(TimeStampedModelMixin, UUIDModel):
    """Подписчики"""

    email = models.EmailField(verbose_name='электронная почта')
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    birthday = models.DateField(verbose_name='дата рождения')

    class Meta:
        verbose_name = "подписчик"
        verbose_name_plural = "подписчики"
        ordering = ("last_name", "first_name")

    def __unicode__(self):
        return "{last_name} {first_name}".format(
            last_name=self.last_name,
            first_name=self.first_name
        )


class Mailing(TimeStampedModelMixin, UUIDModel):
    """Рассылки"""

    subject = models.CharField(max_length=50, verbose_name='тема')
    start_at = models.DateTimeField(verbose_name="дата и время старта рассылки")
    end_at = models.DateTimeField(
        verbose_name="дата и время окончания рассылки"
    )
    template = models.ForeignKey(
        "MailingTemplates",
        on_delete=models.PROTECT,
        verbose_name="рассылка",
        related_name="mailing_templates"
    )
    messages = models.ManyToManyField(
        "Subscribers",
        through="Message",
        through_fields=('mailing', 'subscribers'),
        verbose_name='подписчики'
    )

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        ordering = ("-start_at",)

    def __unicode__(self):
        return "{id}".format(id=self.id)


class Message(TimeStampedModelMixin, UUIDModel):
    """Сообщения"""

    CREATE = "Create"
    SENT = "Sent"
    OPENED = "Opened"

    STATUS = (
        (CREATE, "Сообщение создано"),
        (SENT, "Сообщение успешно отправлено"),
        (OPENED, "Сообщение открыто"),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=CREATE,
        verbose_name="статус отправки сообщения",
    )
    send_at = models.DateTimeField(
        null=True, verbose_name="дата и время отправки сообщения"
    )
    mailing = models.ForeignKey(
        "Mailing",
        on_delete=models.PROTECT,
    )
    subscribers = models.ForeignKey(
        "Subscribers",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __unicode__(self):
        return "Сообщение № {id}".format(id=self.id)


class MailingTemplates(TimeStampedModelMixin, UUIDModel):
    """Шаблоны рассылок"""

    name = models.CharField(max_length=100, help_text='название шаблона для рассылки')
    content = RichTextField()

    class Meta:
        verbose_name = "шаблон рассылки"
        verbose_name_plural = "шаблоны рассылок"

    def __unicode__(self):
        return "Шаблон - {name}".format(name=self.name)

