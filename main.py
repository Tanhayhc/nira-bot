from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن رباتت رو اینجا بذار
TOKEN = "7691696241:AAHdqAtSFrlLbgSWY7xYkKviRxjUubbNJCM"

# آیدی تلگرام خودت (مثلا: 123456789 یا @DarknesHc)
CHAT_ID = "7219776538"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات روشن شد ✅")

async def send_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="پیام تستی از ربات 🚀")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", send_test))

    print("ربات اجرا شد ...")
    app.run_polling()

if __name__ == "__main__":
    main()
