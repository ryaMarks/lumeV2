from tkinter import TRUE
from django.db import models  # importa a manipulação de modelos do django
from django.utils.text import slugify

# Create your models here.

disjuntores = (
    ('25A-MONO', '25A - MONO'),
    ('40A-MONO', '40A - MONO'),
    ('63A-MONO', '63A - MONO'),
    ('40A-TRI', '40A - TRI'),
    ('63A-TRI', '63A - TRI'),
    ('80A-TRI', '80A - TRI'),
    ('100A-TRI', '100A - TRI'),
    ('125A-TRI', '125A - TRI'),
)

class Cliente(models.Model):
    # dados do cliente
    nome = models.CharField('Nome', max_length=100, null=True)
    fone = models.CharField('Telefone', max_length=25, null=True)
    cpf = models.CharField('CPF', max_length=14, null=True)
    rg = models.CharField('RG', max_length=20, null=True)
    nascimento = models.DateField('Nascimento', null=True, blank=True)
    email = models.CharField('Email: ', max_length=50, null=True)
    conta_contrato = models.CharField('Conta Contrato: ', max_length=20, null=True)

    # dados de localização (endereço)
    decimal_x = models.CharField('Decimal - X:', max_length=15, null=True)
    decimal_y = models.CharField('Decimal - Y:', max_length=15, null=True)
    utm_x = models.CharField('UTM - X:', max_length=15, null=True)
    utm_y = models.CharField('UTM - Y:', max_length=15, null=True)
    geografica = models.CharField('Geografica:', max_length=15, null=True)
    adress = models.CharField('Endereço', max_length=200, null=True)
    link_endereco = models.CharField('Link Localização: ', max_length=30, null=True)

    # dados da obra
    inicio = models.DateField('Inicio da obra', null=True, blank=True)
    fim = models.DateField('Fim da obra', null=True, blank=True)
    equipe = models.CharField('Equipe de instalação: ', max_length=300, null=True)

    # dados do sistema
    sis_pot = models.CharField('Potencia do Sistema:', max_length=4, null=True)
    ger_mensal = models.CharField('Geração Mensal:', max_length=8, null=True)
    tipo_padrao = models.CharField('Padrao de entrada:', max_length=10, null=True)
    tipo_geracao = models.CharField('Tipo de geração:', max_length=20, null=True)
    mudar_padrao = models.CharField('Padrao precisa ser mudado ?:', max_length=10, null=True)
    inversor = models.CharField('Inversor(es) Utilizado(s):', max_length=20, null=True)
    qt_inv = models.IntegerField('Quantidade de inversores:', null=True)
    mod = models.CharField('Modulos Utilizados:', max_length=20, null=True)
    qt_mod = models.IntegerField('Quantidade de modulos:', null=True)
    strBx = models.CharField('Modelo de StringBox usada:', max_length=200, null=True)
    qt_strBx = models.IntegerField('Quantidade de stringBox:', null=True)
    disj = models.CharField('Disjuntor de entrada do sistema:', max_length=15, null=True)
    disjSis = models.CharField('Disjuntor de proteção CA do sistema:', max_length=20, null=True)
    dps = models.CharField('DPS CC do Sistema:', max_length=20, null=True)

    # outros dados
    pagamento = models.CharField('Forma de pagamento:', max_length=30, null=True)
    obs = models.CharField('Observações: ', max_length=500, null=True)


    def _str_(self):
        return self
