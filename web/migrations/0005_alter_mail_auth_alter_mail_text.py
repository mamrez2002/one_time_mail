# Generated by Django 5.1.4 on 2024-12-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_mail_auth_alter_mail_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='auth',
            field=models.CharField(default='1d8aceef72855789be283fc7e0b303035aa503b7aa2ca8aa73fd9aa17ff204bd', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='mail',
            name='text',
            field=models.TextField(),
        ),
    ]