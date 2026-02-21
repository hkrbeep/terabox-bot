import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome 👋\n"
        "Send any TeraBox link 🔗"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "terabox" in text:
        await update.message.reply_text(
            "TeraBox link received ✅\n"
            "Feature coming soon ⏳"
        )
    else:
        await update.message.reply_text(
            "Invalid link ❌\n"
            "Send TeraBox link only"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
app.run_polling()
