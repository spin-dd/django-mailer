from django.contrib import admin
from .. import models


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]


@admin.register(models.MailServer)
class MailServerAdmin(BaseAdmin):
    list_display = [f.name for f in models.MailServer._meta.fields]
