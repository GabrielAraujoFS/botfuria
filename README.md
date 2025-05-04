# 🤖 Chatbot do Telegram

Este é um chatbot desenvolvido para o Telegram, com o objetivo de tirar dúvidas dos fãs, responder curiosidades e entender melhor as preferências da comunidade.

## ✨ Funcionalidades

- **Tirar dúvidas**: O bot responde perguntas frequentes dos fãs, esclarecendo informações sobre o time, jogadores e outros tópicos relacionados.
- **Responder curiosidades**: O bot compartilha curiosidades e fatos interessantes sobre o time, jogos, estatísticas e mais.
- **Entender os fãs**: O bot coleta interações para ajudar a compreender melhor as preferências e interesses dos fãs, melhorando a interação com a comunidade.

## 🚀 Tecnologias Utilizadas

- **Linguagem**: Python
- **Biblioteca**: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- **API**: API oficial do Telegram para bots
- **Outras Dependências**: [Outras bibliotecas ou ferramentas que você tenha usado]

## ⚙️ Como Executar Localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   cd nome-do-repositorio
Crie e ative um ambiente virtual (opcional, mas recomendado):

 ```bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:  
Copiar
Editar
pip install -r requirements.txt
 ```
Configure as variáveis de ambiente:

Crie um arquivo .env com o seguinte conteúdo:

ini
Copiar
Editar
TELEGRAM_TOKEN=seu_token_aqui
Execute o bot:

 ```bash
Copiar
Editar
python bot.py
 
 ```
🤖 Como Obter o Token do Bot
Acesse o Telegram e procure por @BotFather

Crie um novo bot com o comando /newbot

Copie o token gerado e insira no seu .env

📦 Estrutura do Projeto
 ```bash
Copiar
Editar
📁 chatbot-telegram 
├── bot.py
├── requirements.txt
├── .env
└── README.md
📌 Observações
Certifique-se de que o bot esteja ativado e tenha permissão para conversar com usuários ou grupos.

O bot pode ser testado no Telegram via @SeuBotUsername

