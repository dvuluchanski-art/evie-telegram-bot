import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я Эйви. Готова помочь тебе 🌒")

# Главный запуск бота
if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")  # Убедись, что переменная окружения задана

    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не установлен!")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
