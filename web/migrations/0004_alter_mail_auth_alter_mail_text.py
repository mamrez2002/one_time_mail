# Generated by Django 5.1.4 on 2024-12-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_mail_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='auth',
            field=models.CharField(default='1b0a54902a3ac270e21d4c4277ef53ec44a5d673f3a37e9f29c980a868c969ec', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='mail',
            name='text',
            field=models.TextField(default='mail'),
        ),
    ]
