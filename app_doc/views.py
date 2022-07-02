from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Cliente
from datetime import date  # biblioteca para coleta de tempo


from app_doc.forms import ClienteForm

#imports para a view pdf
#Django imports
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.


def index(request):
    return render(request, 'index.html')


def cadastro_clientes(request):
    if request.user.is_authenticated:
        form = ClienteForm(request.POST or None)
        context = {
            "form": form
        }
        if form.is_valid():
            form.save()
        return render(request, "cadastro.html", context=context)

    else:
        return redirect("/login/")


class CampoList(ListView):
        model = Cliente
        template_name = 'clientes.html'



# pega a data atual
def getData():
    timer = str(date.today())
    timer_break = timer.split('-')
    meses = {
        1: 'janeiro',
        2: 'feveireiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'}
    mes = meses.get(int(timer_break[1]),)
    data = timer_break[2] + ' de ' + mes + ' de ' + timer_break[0]
    return data


def proc(request, nome):
    if request.user.is_authenticated:
        lista = Cliente.objects.get(nome=nome)
        context = {
            'lista': lista,
            'data': getData(),
        }
        return render(request, 'procuracao.html', context=context)
    else:
        return redirect("/login/")


def users(request, nome):
    if request.user.is_authenticated:
        lista = Cliente.objects.get(nome=nome)
        context = {
            'lista': lista.nome,
        }
        return render(request, 'user.html', context)
    else:
        return redirect("/login/")


def orderService(request, nome):
    if request.user.is_authenticated:
        lista = Cliente.objects.get(nome=nome)
        context = {
            'lista': lista,
        }
        return render(request, 'orderService.html', context)

    else:
        return redirect("/login/")

def void_func():
    pass