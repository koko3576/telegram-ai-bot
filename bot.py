import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import openai

# Carica le variabili da .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise ValueError("Assicurati che TELEGRAM_TOKEN e OPENAI_API_KEY siano impostati nel file .env")

openai.api_key = OPENAI_API_KEY

# Funzione di esempio
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono il tuo bot.")

def main():
    # Creazione dell'applicazione
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Aggiungi i comandi
    app.add_handler(CommandHandler("start", start))

    # Avvia il bot
    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
