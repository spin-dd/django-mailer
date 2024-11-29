from logging import getLogger
import pandas as pd

import djclick as click
from django.utils import translation
from django.core.mail import EmailMessage, get_connection

from ... import models

log = getLogger()

translation.activate("ja")


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument("server_name")
@click.argument("template_name")
@click.argument("excel_path")
@click.option("--to_fieild", "-t", default="to")
@click.pass_context
def send_batch(ctx, server_name, template_name, excel_path, to_fieild):
    """メールを送信する"""
    server = models.MailServer.objects.filter(name=server_name).first()
    if not server:
        print(f"{server_name}のサーバー設定がありません")
        return
    template = models.EmailTemplate.objects.filter(name=template_name).first()
    if not template:
        print(f"{template_name}のメールテンプレート設定ががありません")
        return

    connection = server.get_connection()

    def send_row(row):
        ctx = row.to_dict()
        to = ctx.get(to_fieild, None)
        if not to:
            return
        template.send(to=[to], connection=connection, ctx=ctx)

    data = pd.read_excel(excel_path, dtype="str")
    data.apply(send_row, axis=1)
