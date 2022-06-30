from tkinter import TRUE
from django.db import models  # importa a manipulação de modelos do django
from django.utils.text import slugify

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100, null=True)
    fone = models.CharField('Telefone', max_length=11, null=True)
    cpf = models.CharField('CPF', max_length=14, null=True)
    rg = models.CharField('RG', max_length=20, null=True)
    nascimento = models.DateField('Nascimento', null=True, blank=True)
    email = models.CharField('Email: ', max_length=20, null=True)
    conta_contrato = models.CharField('Conta Contrato: ', max_length=20, null=True)
    decimal_x = models.CharField('Decimal - X:', max_length=15, null=True)
    decimal_y = models.CharField('Decimal - Y:', max_length=15, null=True)
    utm_x = models.CharField('UTM - X:', max_length=15, null=True)
    utm_y = models.CharField('UTM - Y:', max_length=15, null=True)
    geografica = models.CharField('Geografica:', max_length=15, null=True)
    adress = models.CharField('Endereço', max_length=200, null=True)
    link_endereco = models.CharField('Link Localização: ', max_length=30, null=True)
    sis_pot = models.CharField('Potencia do Sistema:', max_length=4, null=True)
    ger_mensal = models.CharField('Geração Mensal:', max_length=8, null=True)
    tipo_padrao = models.CharField('Padrao de entrada:', max_length=10, null=True)
    tipo_geracao = models.CharField('Tipo de geração:', max_length=20, null=True)
    mudar_padrao = models.BooleanField('Padrao precisa ser mudado ?:', null=True)
    inversor = models.CharField('Inversor(es) Utilizado(s):', max_length=20, null=True)
    qt_inv = models.IntegerField('Quantidade de inversores:', null=True)
    mod = models.CharField('Modulos Utilizados:', max_length=20, null=True)
    qt_mod = models.IntegerField('Quantidade de modulos:', null=True)

    def _str_(self):
        return self
