from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Timestamp(models.Model):
    created_at = models.DateTimeField(
        _("Created At"), help_text=_("Created At Help"), default=now
    )
    updated_at = models.DateTimeField(
        _("Updated At"), help_text=_("Updated At Help"), auto_now=True
    )

    class Meta:
        abstract = True


class MailServer(Timestamp):
    name = models.CharField("名称", max_length=100)
    host = models.CharField("ホスト", max_length=100)
    post = models.PositiveSmallIntegerField("ポート", default=25)
    username = models.CharField(
        "ユーザー名", max_length=100, default=None, blank=True, null=True
    )
    password = models.CharField(
        "パスワード", max_length=100, default=None, blank=True, null=True
    )
    use_tls = models.BooleanField("TLS", default=False)
    use_ssl = models.BooleanField("SSL", default=False)

    class Meta:
        verbose_name = "サーバー"
        verbose_name_plural = "サーバー"

    def __str__(self):
        return self.name
