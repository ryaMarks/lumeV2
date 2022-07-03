
# Descriçaõ deste arquivo: Este arquivo são executadas as funções de backEnd; aqui esta a magica das coisas.
# Aqui são feitos os redirecionamentos de paginas, checagem de autenticação, alteraões no banco de dados,
# funções de callback, cadastro de usuarios e etc. Ou seja, tudo que diz respeito as atividades dinamicas não
# exibidas ao usuario convencional


# -------------------------------------------------------------------------------------------------------------
# --------------------------------- importa os modulos que serao utilizados ------------------------------------
# -------------------------------------------------------------------------------------------------------------
from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse  # importa biblioteca que pega a resposta html
from django.views.generic.list import ListView  # importa biblioteca para exibir listas
from django.views.generic import View
# arquivos auxiliares que serão utilizados aqui
from .models import Cliente  # importa a classe Cliente do arquivo .models
from app_doc.forms import ClienteForm  # importa a classe ClienteForm do arquivo forms dentro da pasta app_doc
from datetime import date  # biblioteca para coleta de tempo
# importa a biblioteca do WeasyPrint (gerar PDF de páginas html)
from weasyprint import CSS, HTML, Attachment  # importa biblioteca do weasyprint para arquivos estaticos
# -------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------
# ------------------------------------------ criando funções de BackEnd ---------------------------------------
# -------------------------------------------------------------------------------------------------------------
# função inicial (retorna a primeira pagina assim que  o usuario acessa a aplicação
def index(request):
    return render(request, 'index.html')  # retorna pagina inicial


# função que faz o cadastro de clientes no banco de dados
def cadastro_clientes(request):
    if request.user.is_authenticated:  # se o usuario estiver autenticado (logado)
        form = ClienteForm(request.POST or None)  # carrega o formulario que esta cadastrado em ClientForm
        context = {  # variavel que carrega os dados para o html
            "form": form  # passa os dados do cliente que serao enviados para o html
        }
        if form.is_valid():  # se o formulario enviado for valido
            form.save()  # salva os dados do formulario (cadastra o cliente)
        return render(request, "cadastro.html", context=context)  # retorna para a pagina inicial
    else:  # se o usuario nao estiver autenticado (logado)
        return redirect("/login/")  # manda para a pagina de login


#  classe que retorna os usuarios cadastrados
class CampoList(ListView):
        model = Cliente
        template_name = 'clientes.html'


# pega a data atual
def getData():
    timer = str(date.today())  # pega a data atual em forma de string
    timer_break = timer.split('-')  # quebra a string em componentes separados por '-'
    meses = {  # vetor com os meses referentes aos numeros
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
    mes = meses.get(int(timer_break[1]),)  # pega o mes atual por extenso
    data = timer_break[2] + ' de ' + mes + ' de ' + timer_break[0]  # gera a data total
    return data  # retorna a data total


# função que retorna o usuario selecionado
def user(request, nome):  # recebe a solicitacao html e o nome do usuario
    if request.user.is_authenticated:  # se o usuario estiver autenticado (logado)
        lista = Cliente.objects.get(nome=nome)  # pega os dados do cliente com o nome e salva em 'lista'
        context = {  # variavel que carrega os dados para o html
            'lista': lista.nome,  # passa os dados do cliente que serao enviados para o html
        }
        return render(request, 'user.html', context)  # retorna a pagina do usuario
    else:  # se o usuario nao estiver autenticado (logado)
        return redirect("/login/")   # manda para a pagina de login


# função que gera ordem de serviço automatica
def orderService(request, nome):  # recebe a solicitacao html e o nome do usuario
    if request.user.is_authenticated:  # se o usuario estiver autenticado (logado)
        lista = Cliente.objects.get(nome=nome)  # pega os dados do cliente com o nome e salva em 'lista'
        context = {  # variavel que carrega os dados para o html
            'lista': lista,  # passa os dados do cliente que serao enviados para o html
        }
        return render(request, 'orderService.html', context)  # retorna a ordem de servico preenchida
    else:  # se o usuario nao estiver autenticado (logado)
        return redirect("/login/")   # manda para a pagina de login


def procuracao(request, nome):  # recebe a solicitacao html e o nome do usuario
    if request.user.is_authenticated:  # se o usuario estiver autenticado (logado)
        lista = Cliente.objects.get(nome=nome)  # pega os dados do cliente com o nome e salva em 'lista'
        context = {  # variavel que carrega os dados para o html
            'lista': lista,  # passa os dados do cliente que serao enviados para o html
            'data': getData(),  # carrega a data atual no documento
        }
        html_template = render(request, 'procuracao.html', context=context)  # prepara o template html
        html = HTML(string=html_template)
        pdf = html.write_pdf()  # transforma html em pdf
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = 'filename="procuracao.pdf"'
        return response
    else:  # se o usuario nao estiver autenticado (logado)
        return redirect("/login/")   # manda para a pagina de login


def pdf_generate(request):
    html_template = get_template('procuracao.html').render()
    html = HTML(string=html_template)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="procuracao.pdf"'
    return response

