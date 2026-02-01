import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai

# Prendi le variabili d'ambiente (su Railway le aggiungi nella sezione "Environments")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise ValueError("Assicurati che TELEGRAM_TOKEN e OPENAI_API_KEY siano impostati nelle Variables di Railway")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono il tuo bot GPT.")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Scrivi qualcosa dopo /ask")
        return

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    await update.message.reply_text(answer)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))

    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
