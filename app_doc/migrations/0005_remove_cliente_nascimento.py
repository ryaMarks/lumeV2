# Generated by Django 3.2.13 on 2022-06-23 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0004_auto_20220617_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nascimento',
        ),
    ]
