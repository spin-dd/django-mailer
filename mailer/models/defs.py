from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Timestamp(models.Model):
    created_at = models.DateTimeField(_("Created At"), help_text=_("Created At Help"), default=now)
    updated_at = models.DateTimeField(_("Updated At"), help_text=_("Updated At Help"), auto_now=True)

    class Meta:
        abstract = True


class MailServer(Timestamp):
    name = models.CharField("名称", max_length=100)
    host = models.CharField("ホスト", max_length=100)
    port = models.PositiveSmallIntegerField("ポート", default=25)
    username = models.CharField("ユーザー名", max_length=100, default=None, blank=True, null=True)
    password = models.CharField("パスワード", max_length=100, default=None, blank=True, null=True)
    use_tls = models.BooleanField("TLS", default=False)
    use_ssl = models.BooleanField("SSL", default=False)

    class Meta:
        abstract = True


class EmailBase(models.Model):
    to = models.CharField(
        verbose_name=_("To"),
        max_length=1000,
        blank=True,
        null=True,
    )

    cc = models.CharField(
        verbose_name=_("Copy to"),
        max_length=1000,
        blank=True,
        null=True,
    )

    bcc = models.CharField(
        verbose_name=_("Blind copy"),
        max_length=1000,
        blank=True,
        null=True,
    )

    from_email = models.EmailField(verbose_name=_("From"), help_text=_("Sender's email address."))

    subject = models.CharField(
        verbose_name=_("Subject"),
        max_length=140,
    )

    body = CKEditor5Field(
        verbose_name=_("Body"),
        blank=True,
        null=True,
    )

    reply_to = models.CharField(
        verbose_name=_("Reply to"),
        max_length=1000,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class EmailTemplate(EmailBase, Timestamp):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=50,
        unique=True,
    )

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=100,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
