# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


class TimeStampedModelMixin(models.Model):
    """Абстрактная модель, добавляющая дату создания и дату изменения."""

    created_at = CreationDateTimeField(verbose_name="дата создания")
    updated_at = ModificationDateTimeField(verbose_name="дата изменения")

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """Абстрактная модель, добавляющая уникальный идентификатор"""

    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        help_text="Уникальный идентификатор. Генерируется системой автоматически.",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{name}:{hex}".format(name=self.__class__.__name__,
                                     hex=self.id.hex)
