# Generated by Django 4.0.5 on 2022-06-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0009_alter_cliente_disj_alter_cliente_mudar_padrao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='equipe',
            field=models.DateField(max_length=300, null=True, verbose_name='Equipe de instalação: '),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fim',
            field=models.DateField(blank=True, null=True, verbose_name='Fim da obra: '),
        ),
        migrations.AddField(
            model_name='cliente',
            name='inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Inicio da obra: '),
        ),
        migrations.AddField(
            model_name='cliente',
            name='qt_strBx',
            field=models.IntegerField(null=True, verbose_name='Quantidade de stringBox:'),
        ),
    ]
