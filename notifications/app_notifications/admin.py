# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app_notifications.models import Subscribers, Mailing, MailingTemplates, Message


class SubscribersAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'birthday'
    )


class MailingTemplatesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content'
    )


class MailingAdmin(admin.ModelAdmin):
    list_display = (
        'start_at',
        'end_at',
        'template',
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'send_at',
        'status',
        'mailing',
        'subscribers'
    )

    readonly_fields = (
        'send_at',
        'status',
        'mailing',
        'subscribers'
    )

    list_filter = ("status",)


admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(MailingTemplates, MailingTemplatesAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)
