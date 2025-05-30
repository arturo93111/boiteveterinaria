from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from archivotron import obtener_citas
from dotenv import load_dotenv
import os

# variables de entorno
load_dotenv()
token_telegram = os.getenv("token")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐾 ¡Hola! Soy el bot de la veterinaria.\n\n"
        "Envía:\n"
        "👉 /hoy - para ver las citas de hoy\n"
        "👉 /manana - para ver las citas de mañana"
    )

# Comando /hoy
async def citas_hoy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = obtener_citas("hoy")
    await update.message.reply_text(resultado)

# Comando /manana
async def citas_manana(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = obtener_citas("mañana")
    await update.message.reply_text(resultado)

#  app del bot
def main():
    app = Application.builder().token(token_telegram).build()

    # Handlers de comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hoy", citas_hoy))
    app.add_handler(CommandHandler("manana", citas_manana))

    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
