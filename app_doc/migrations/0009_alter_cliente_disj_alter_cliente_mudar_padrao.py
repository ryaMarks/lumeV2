# Generated by Django 4.0.5 on 2022-06-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0008_cliente_disjsis_cliente_dps_cliente_obs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='disj',
            field=models.CharField(max_length=15, null=True, verbose_name='Disjuntor de entrada do sistema:'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mudar_padrao',
            field=models.CharField(max_length=10, null=True, verbose_name='Padrao precisa ser mudado ?:'),
        ),
    ]
