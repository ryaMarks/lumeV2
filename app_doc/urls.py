from django.urls import path
from .views import index, cadastro_clientes, CampoList, users, orderService, procuracao, clientTrello


urlpatterns = [
    path('', index, name="lumeenergia"),
    path('cadastro/', cadastro_clientes),
    path('clientes/', CampoList.as_view()),
    path('clientes/<nome>', users),
    path('clientes/<nome>/ordemServico/', orderService),
    path('clientes/<nome>/procuracao/', procuracao),
    path('trello', clientTrello)
]
