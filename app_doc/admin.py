from django.contrib import admin

# Register your models here.

from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf','fone', 'conta_contrato', )

admin.site.register(Cliente, ClienteAdmin)
