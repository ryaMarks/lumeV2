# programa que carrega os dados do Quadro de projeto da Lume
from trello import TrelloClient
quadro = '5e38560cdfeead83a2ec6666'  # chave de acesso do trello de projetos (quadro projetos  Lume)
client = TrelloClient(  # carrega as credenciais de acesso do trello
    api_key='4a2f58cd107e7e8efd754acb3b360faf',
    token='0b4deaa5026d7a812138edd219b42b53897f4c21c9c62927bf1157e44ca4e451'
)
user = []  # faz o primeiro tratamento de dados
geral = []  # faz o segundo tratamento de dados



def getClientData(cliente):
    geral = []  # faz o segundo tratamento de dados
    c = []
    board = client.get_board(quadro)
    cartoes = board.get_cards()
    for cartao in cartoes:
        if cartao.name == cliente:
            dados = str(cartao.desc).split('\n')
            dados.pop(8)
            for i in dados:
                if i != '':
                    user.append(i)
            user.pop(11)
            for valor in user:
                detalhado = valor.split(':')
                for j in detalhado:
                    geral.append(j)
    geral.remove(' ')
    for i in range(0, 38):
        if i > 0:
            if (i % 2) != 0:
                c.append(geral[i])
    clientData = {
        'nome': c[0],
        'rg': c[1],
        'cpf': c[2],
        'nascimento': c[3],
        'contaContrato': c[4],
        'endereco': c[5],
        'telefone': c[6],
        'email': c[7],
        'decimal': c[8],
        'geografica': c[9],
        'utm': c[10],
        'sisPot': c[11],
        'inversor': c[12],
        'paineis': c[13],
        'gMensal': c[14],
        'valor_servico': c[15],
        'ligacao': c[16],
        'modalidade': c[17],
    }
    return clientData

def clientsNome():
    clientes = []
    board = client.get_board(quadro)
    cartoes = board.get_cards()
    for cartao in cartoes:
        clientes.append(cartao.name)
    clientes.remove('MODELO DE CARD - ATÉ 10 KW')
    clientes.remove('MODELO DE CARD - ACIMA DE 10 KW')
    return clientes