# 🤖 TrelloPilot

> Agente inteligente com **Google Gemini** que automatiza seu fluxo de trabalho no Trello — criando e movendo cards com base em contexto, regras ou comandos em linguagem natural.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Gemini](https://img.shields.io/badge/LLM-Gemini%20API-orange?logo=google)
![Trello](https://img.shields.io/badge/Integração-Trello%20API-blue?logo=trello)

---

## 📌 Sobre

**TrelloPilot** é um agente em Python que se conecta ao seu Trello e automatiza o gerenciamento de tarefas repetitivas. Em vez de criar e organizar cards manualmente, você descreve o que precisa ser feito — e o agente resolve usando o Gemini.

**Exemplos de uso:**
- *"Crie um card para a nova solicitação de feature na lista Backlog"*
- Mover cards automaticamente para *Concluído* quando uma condição for atendida
- Criar vários cards de uma vez a partir de uma lista de tarefas

---

## ✨ Funcionalidades

- 🧠 **Decisões baseadas em IA** — Usa o Gemini para interpretar comandos e contexto
- 📋 **Criação de cards** — Cria cards automaticamente com título, descrição, etiquetas e prazo
- 🔀 **Movimentação de cards** — Move cards entre listas com base em regras ou linguagem natural
- 🔌 **Integração com Trello** — Conexão completa via API REST oficial do Trello
- 🔒 **Configuração segura** — Credenciais gerenciadas via arquivo `.env`

---

## 🛠️ Tecnologias

| Tecnologia | Função |
|---|---|
| Python 3.10+ | Linguagem principal |
| Google Gemini API | LLM / agente de IA |
| Trello REST API | Integração com o board |
| `python-dotenv` | Gerenciamento de variáveis de ambiente |
| `requests` | Cliente HTTP |

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto, certifique-se de ter:

- Python **3.10 ou superior** instalado
- Uma conta no **Trello** com API Key e Token ([obtenha aqui](https://trello.com/power-ups/admin))
- Uma **chave de API do Google Gemini** ([obtenha aqui](https://aistudio.google.com/app/apikey))

---

## 🚀 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/trello-pilot.git
cd trello-pilot

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto com base no exemplo abaixo:

```env
# .env

# Trello
TRELLO_API_KEY=sua_api_key_do_trello
TRELLO_TOKEN=seu_token_do_trello
TRELLO_BOARD_ID=id_do_seu_board

# Google Gemini
GEMINI_API_KEY=sua_api_key_do_gemini
```

> ⚠️ Nunca suba o arquivo `.env` para o repositório. Ele já está listado no `.gitignore`.

---

## ▶️ Como usar

```bash
python main.py
```

Você também pode passar um comando diretamente:

```bash
python main.py --command "Mova todos os cards de 'Em Andamento' com mais de 7 dias para 'Revisão'"
```

Ou usar o modo interativo:

```bash
python main.py --interactive
```

---

## 📁 Estrutura do Projeto

```
trello-pilot/
├── agent/
│   ├── __init__.py
│   ├── gemini_agent.py     # Integração com o Gemini e gerenciamento de prompts
│   └── trello_tools.py     # Ações na API do Trello (criar, mover, listar)
├── config/
│   └── settings.py         # Carregamento das variáveis de ambiente
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

1. Faça um fork do projeto
2. Crie sua branch: `git checkout -b feature/minha-feature`
3. Commit suas alterações: `git commit -m 'feat: adiciona minha feature'`
4. Envie para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

Feito por [Heitor](https://github.com/heitorcavss)
