import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)
from openai import OpenAI


# ==========================
# 1. Leggiamo le variabili da Render
# ==========================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise ValueError(
        "ERRORE: Devi impostare TELEGRAM_TOKEN e OPENAI_API_KEY su Render"
    )


# ==========================
# 2. Client OpenAI moderno
# ==========================
client = OpenAI(api_key=OPENAI_API_KEY)


# ==========================
# 3. Funzione risposta messaggi
# ==========================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )

    reply = response.choices[0].message.content
    await update.message.reply_text(reply)


# ==========================
# 4. Avvio bot
# ==========================
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("✅ Bot avviato correttamente!")
    app.run_polling()


if __name__ == "__main__":
    main()
