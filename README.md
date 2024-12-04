# django-mailer

## .env作成

直下のファオルダにファイルを登録します.

例:

~~~ini
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=<admin@example.com>
DJANGO_SUPERUSER_PASSWORD=Aiy6mi3o
~~~

## 起動

~~~bash
docker compose up -d
~~~

## テーブル作成

```bash
docker compose run --rm mailer python web/manage.py migrate
```

## 管理者登録

.envの `SUPERUSER` の内容で登録されます

```bash
docker compose run --rm mailer python web/manage.py createsuperuser --noinput
```

## メールサーバー登録

- <http://localhost:8000/admin/> で .env のSUPERUSERでログイン
- <http://localhost:8000/admin/mailer/mailserver/> でサーバー登録

## テンプレート登録

- [一括送信コマンド/テンプレート](<https://github.com/spin-dd/django-mailer/pull/2>) の内容でテンプレートを作成
- <http://localhost:8000/admin/mailer/emailtemplate/> でテンプレート登録

## Excelファイル作成

- [一括送信コマンド/テンプレート](<https://github.com/spin-dd/django-mailer/pull/2>) の内容でExcelを作成
- 直下に .secrets フォルダーを作成し、そこにExcelファイルをおく

## 一括送信

-
- [一括送信コマンド/テンプレート](<https://github.com/spin-dd/django-mailer/pull/2>) の内容で作成したExcelの宛先にメールを送信する。

例: メールサーバー名が `cloudserver` , テンプレート名が `app_download`, Excelの宛先カラムが `to` の場合

~~~bash
docker compose run --rm mailer python web/manage.py mailer send-batch cloudserver app_download .secrets/mails.xlsx -t to 
~~~

## 削除

~~~bash
docker compose down --rmi all --volumes --remove-orphans
~~~
