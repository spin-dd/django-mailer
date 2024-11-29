from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import get_connection
from . import defs
from ..utils import render
from .interface import MailAttachment, MailMessage


class MailServer(defs.MailServer):

    class Meta:
        verbose_name = "サーバー"
        verbose_name_plural = "サーバー"

    def __str__(self):
        return self.name

    def get_connection(self):
        """接続"""
        return get_connection(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            use_tls=self.use_tls,
            use_ssl=self.use_ssl,
        )


class EmailTemplate(defs.EmailTemplate):
    class Meta:
        verbose_name = _("Email Template")
        verbose_name_plural = _("Email Templates")

    def __str__(self):
        return self.title

    def send(
        self,
        to=None,
        cc=None,
        bcc=None,
        reply_to=None,
        from_email=None,
        attachment_set=None,
        connection=None,
        ctx=None,
    ):
        ctx = ctx or {}

        subject = render(self.subject, **ctx)
        body = render(self.body, **ctx)

        cc = cc or self.cc
        bcc = bcc or self.bcc
        cc = cc and cc.spit(",") or None
        bcc = bcc and bcc.spit(",") or None

        reply_to = reply_to or self.reply_to
        from_email = from_email or self.from_email
        attachment_set = (
            isinstance(attachment_set, list)
            and [MailAttachment(name=i[0], path=i[1]) for i in attachment_set]
            or []
        )

        msg = MailMessage(
            from_email=from_email,
            to=to,
            cc=cc,
            bcc=bcc,
            reply_to=reply_to,
            attachment_set=attachment_set,
        )
        return msg.send(subject, body, html=True, connection=connection)
