import telebot

BOT_TOKEN = '8159278920:AAGcEl7tKwqBFEF2i4XMPy7k5PWELbwOx44'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def boas_vindas(message):
    texto = (
        "👋 Fala, torcedor da FURIA!🐆\n\n"
        "Sou o *Bot da FURIA* e posso te ajudar com perguntas como:\n"
        "- Quem são os jogadores?\n"
        "- Quando é o próximo jogo?\n"
        "- Onde comprar produtos oficiais?\n"
        "- Como participar do FURIA Nation?\n\n"
        "É só me mandar sua pergunta! 💜🖤"
    )
    bot.reply_to(message, texto, parse_mode='Markdown')

# 📂 Base de conhecimento com palavras-chave por pergunta
faq = {

    "jogadores": {
        "keywords": ["jogadores", "line", "line-up", "player", "time"],
        "resposta": "👥 A line de CS2 da FURIA conta com: *KSCERATO*, *yuurih*, *chelo*, *arT* e *FalleN*."
    },
    "proximo_jogo": {
        "keywords": ["próximo jogo", "agenda", "quando joga", "jogo", "partida"],
        "resposta": "📅 Você pode ver a agenda atualizada da FURIA aqui: [Agenda FURIA](https://furia.gg)"
    },
    "loja": {
        "keywords": ["loja", "camiseta", "roupa", "produto", "comprar"],
        "resposta": "🛒 Os produtos oficiais estão disponíveis em: [loja.furia.gg](https://loja.furia.gg)"
    },
    "desconto": {
        "keywords": ["desconto", "furia nation", "benefício", "vantagem"],
        "resposta": "🎁 Membros do *FURIA Nation* têm descontos exclusivos. Saiba mais em [furianation.gg](https://furianation.gg)"
    },
    "historia": {
        "keywords": ["história", "fundação", "quando começou", "origem"],
        "resposta": "📖 A FURIA foi fundada em *2017* e é hoje uma das maiores organizações de esports do Brasil."
    },
    "discord": {
        "keywords": ["discord", "comunidade", "chat", "grupo"],
        "resposta": "🎤 Entra no nosso Discord oficial: [discord.gg/furia](https://discord.gg/furia)"
    },
    "contato": {
        "keywords": ["contato", "falar", "suporte", "ajuda"],
        "resposta": "📬 Pode falar com a equipe pelo site: [furia.gg](https://furia.gg)"
    },
    "redes": {
        "keywords": ["redes sociais", "instagram", "twitter", "tiktok", "youtube"],
        "resposta": "📱 Nos siga nas redes: Twitter, Instagram, TikTok e YouTube — @FURIA"
    }
}

# 📩 Função para responder mensagens com base nos sinônimos
@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    resposta = None

    for categoria in faq.values():
        if any(palavra in texto for palavra in categoria["keywords"]):
            resposta = categoria["resposta"]
            break

    if resposta:
        bot.reply_to(message, resposta, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❓ Não entendi sua pergunta. Tente algo como 'loja', 'próximo jogo' ou 'jogadores'.")

bot.polling()
