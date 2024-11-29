import json
from concurrent.futures import ThreadPoolExecutor
from mimetypes import guess_type
from typing import List, Optional

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from pydantic import BaseModel, EmailStr


class MailAttachment(BaseModel):
    """添付ファイル"""

    name: str = ""
    path: str = ""

    class Config:
        arbitrary_types_allowed = True

    def attach_to(self, message):
        mtype, _x = guess_type(self.path)
        content = open(self.path, mode="rb").read()
        message.attach(self.name, content, mtype)


class MailMessage(BaseModel):
    """テンプレート"""

    # https://docs.djangoproject.com/en/3.2/topics/email/#emailmessage-objects
    from_email: EmailStr
    to: Optional[List[EmailStr]] = []
    cc: Optional[List[EmailStr]] = []
    bcc: Optional[List[EmailStr]] = []
    reply_to: Optional[EmailStr] = None
    attachment_set: Optional[List[MailAttachment]] = []

    class Config:
        arbitrary_types_allowed = True

    @property
    def email_params(self):
        # from pydantic.json import pydantic_encoder
        # return json.loads(json.dumps(self, default=pydantic_encoder))
        return json.loads(self.json())

    def send(self, subject, body, html=True, connection=None):
        def _background(msg):
            msg.send()

        params = self.email_params
        params.pop("attachment_set", None)
        msg = EmailMultiAlternatives(subject=subject, connection=connection, **params)
        if html:
            msg.attach_alternative(body, "text/html")
        else:
            msg.body = body

        for attachment in self.attachment_set:
            attachment.attach_to(msg)

        if getattr(settings, "IN_TEST", False):
            msg.send()
        else:
            executor = ThreadPoolExecutor(max_workers=1)
            executor.submit(_background, msg)
        return
