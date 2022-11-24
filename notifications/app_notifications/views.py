# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64

from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

from app_notifications.models import Message

# изображение прозрачное - 1px
image_bytes = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAACnej3aAAAAAXRSTlMAQObYZgAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII='


class ImageOutputView(View):
    """Отдача изображения и смена статуса сообщения на Открыто"""
    def get(self, request):
        # извлечение message_id из url
        message_id_hex = request.path[
                         len(reverse("image_output")):
                         len(reverse("image_output")) + 32
                         ]
        # изменение статуса сообщения на Opened
        message = Message.objects.filter(~Q(status=Message.OPENED), id=message_id_hex).first()
        if message:
            message.status = Message.OPENED
            message.save(update_fields=["updated_at", "status"])
        return HttpResponse(base64.b64decode(image_bytes), content_type="image/png")
