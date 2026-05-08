from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from google.adk.tools.agent_tool import AgentTool
from datetime import date
from dotenv import load_dotenv
import os

#Funções: adicionar tarefas c/ nome e descrição, listar tarefas ou filtrar por status, marcar tarefas como concluídas, remover tarefas da lista, mudar status da tarefa('a fazer' -> 'em andamento' -> 'concluído'), gerar contexto temporal p/ organizar as tarefas do dia.
load_dotenv()  
#Load das credenciais Trello
API_KEY = os.getenv('API_KEY_TRELLO')
API_TOKEN = os.getenv('TOKEN_TRELLO')
API_SECRET = os.getenv('SECRET_KEY_TRELLO')


def get_current_date():
    data_atual = date.today()
    data_formatada = data_atual.strftime("%d/%m/%Y")
    return data_formatada

def add_task(nome_task: str, desc_task: str, date_task: str):
    #conexão c/ Trello
    client = TrelloClient(
        api_key=API_KEY,
        token=API_TOKEN,
        api_secret=API_SECRET
    )
    boards = client.list_boards()
    meu_board = [b for b in boards if b.name == 'DIO-AI'][0]
    
    listas = meu_board.list_lists() #list_lists() retorna as listas do board
    minha_lista = [l for l in listas if l.name.upper() == 'A FAZER'][0]
    
    #Criar o card
    minha_lista.add_card(
        name=nome_task,
        desc=desc_task + ' - ' + date_task
    )
    
    
def list_tasks(status: str = 'todas'):
    client = TrelloClient(
        api_key=API_KEY,
        token=API_TOKEN,
        api_secret=API_SECRET
    )
    boards = client.list_boards()
    meu_board = [b for b in boards if b.name == 'DIO-AI'][0]
    
    listas = meu_board.list_lists() #list_lists() retorna as listas do board
    
    if status.upper() == 'A FAZER':
        minha_lista = [l for l in listas if l.name.upper() == 'A FAZER']  # sem [0]
    elif status.upper() == 'EM ANDAMENTO':
        minha_lista = [l for l in listas if l.name.upper() == 'EM ANDAMENTO']
    elif status.upper() == 'CONCLUÍDO':
        minha_lista = [l for l in listas if l.name.upper() == 'CONCLUÍDO']
    else:
        minha_lista = listas
        
    tarefas = []
    for lista in minha_lista:
        cards = lista.list_cards()
        for card in cards:
            tarefas.append({
                'nome': card.name,
                'descricao': card.desc,
                'status': lista.name
            })
    
    return tarefas
    
    
def muda_stts(nome_task: str, novo_status: str) -> str:
    try:
        client = TrelloClient(
            api_key=API_KEY,
            token=API_TOKEN,
            api_secret=API_SECRET
        )
        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == 'DIO-AI'][0]
        listas = meu_board.list_lists()
        
        mapa_status = {
            'a fazer': 'A FAZER',
            'em andamento': 'EM ANDAMENTO',
            'concluído': 'CONCLUÍDO'
        }
        
        nome_lista_destino = mapa_status.get(novo_status.lower())
        
        if not nome_lista_destino:
            return f"Status '{novo_status}' inválido. Use 'a fazer', 'em andamento' ou 'concluído'."
        
        lista_destino = next(
            (l for l in listas if l.name.upper() == nome_lista_destino), 
            None
        )
        
        if not lista_destino:
            return f"Lista '{nome_lista_destino}' não encontrada no Trello."
        
        # busca card
        card_encontrado = None
        lista_origem = None
        for lista in listas:
            cards = lista.list_cards()
            card_encontrado = next(
                (c for c in cards if c.name == nome_task), 
                None
                )
            if card_encontrado:
                lista_origem = lista
                break
            
        if not card_encontrado:
            return f"Tarefa '{nome_task}' não encontrada em nenhuma lista."
            
        card_encontrado.change_list(lista_destino.id)
        
        return f"Tarefa '{nome_task}' movida para '{novo_status}'."
    
    except Exception as e:
        return f"Erro ao mudar status da tarefa: {str(e)}"

def remove_task(nome_task: str) -> str:
    try:
        client = TrelloClient(
            api_key=API_KEY,
            token=API_TOKEN,
            api_secret=API_SECRET
        )
        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == 'DIO-AI'][0]
        listas = meu_board.list_lists()
        
        card_encontrado = None
        for lista in listas:
            cards = lista.list_cards()
            card_encontrado = next(
                (c for c in cards if c.name == nome_task), 
                None
                )
            if card_encontrado:
                break
            
        if not card_encontrado:
            return f"Tarefa '{nome_task}' não encontrada em nenhuma lista."
        
        card_encontrado.delete()
        
        return f"Tarefa '{nome_task}' removida com sucesso."
    
    except Exception as e:
        return f"Erro ao remover tarefa: {str(e)}"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Agente organizador de tarefas.',
    instruction='''
        Você é um agente organizador de tarefas. 
        Sua função é receber o nome de uma tarefa e sua descrição e criar um card no Trello.
        Você deve me perguntar que atividades eu tenho no dia e criar um card para cada uma delas.
        Você inicia a conversa assim que for ativado, perguntando quais são as atividades do dia.
        Sempre inicia a conversa perguntando as atividades do dia informando a data pela tool get_current_date,
        e siga perguntando se tem mais atividades até o usuário informar que não tem mais atividades.
        Suas funções/tools disponíveis são:
        
        
        1) Adicionar novas tarefas com nome e descrição.
        2) Listar tarefas ou filtrar por status.
        3) Marcar tarefas como concluídas. 
        4) Remover tarefas da lista.
        5) Mudar status da tarefa('a fazer' -> 'em andamento' -> 'concluído').
        6) Gerar contexto temporal para organizar as tarefas do dia.
    ''',
    tools=[add_task, get_current_date, list_tasks, muda_stts, remove_task]
    
)
