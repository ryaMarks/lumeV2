# Generated by Django 3.2.13 on 2022-06-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0005_remove_cliente_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Nascimento'),
        ),
    ]