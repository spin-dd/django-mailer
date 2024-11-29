# Generated by Django 5.1.3 on 2024-11-29 01:56

import django.utils.timezone
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Created At Help', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At Help', verbose_name='Updated At')),
                ('to', models.CharField(blank=True, max_length=1000, null=True, verbose_name='To')),
                ('cc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Copy to')),
                ('bcc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Blind copy')),
                ('from_email', models.EmailField(help_text="Sender's email address.", max_length=254, verbose_name='From')),
                ('subject', models.CharField(max_length=140, verbose_name='Subject')),
                ('body', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Body')),
                ('reply_to', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Reply to')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Email Template',
                'verbose_name_plural': 'Email Templates',
            },
        ),
        migrations.CreateModel(
            name='MailServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Created At Help', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated At Help', verbose_name='Updated At')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('host', models.CharField(max_length=100, verbose_name='ホスト')),
                ('port', models.PositiveSmallIntegerField(default=25, verbose_name='ポート')),
                ('username', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='ユーザー名')),
                ('password', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='パスワード')),
                ('use_tls', models.BooleanField(default=False, verbose_name='TLS')),
                ('use_ssl', models.BooleanField(default=False, verbose_name='SSL')),
            ],
            options={
                'verbose_name': 'サーバー',
                'verbose_name_plural': 'サーバー',
            },
        ),
    ]
