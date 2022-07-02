from django.urls import path
from .views import index, cadastro_clientes, CampoList, proc, users, orderService


urlpatterns = [
    path('', index, name="lumeenergia"),
    path('cadastro/', cadastro_clientes),
    path('clientes/', CampoList.as_view()),
    path('clientes/<nome>', users),
    path('clientes/<nome>/procuracao/', proc),
    path('clientes/<nome>/ordemServico/', orderService),
]