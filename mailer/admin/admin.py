from django.contrib import admin

from .. import models


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]


@admin.register(models.MailServer)
class MailServerAdmin(BaseAdmin):
    list_display = [f.name for f in models.MailServer._meta.fields]


@admin.register(models.EmailTemplate)
class EmailTemplateAdmin(BaseAdmin):
    list_display = [f.name for f in models.EmailTemplate._meta.fields]
