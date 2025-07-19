import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, ContextTypes, CommandHandler
)
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

# Логирование
logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я Эйви. Готова помочь тебе 🖤")

# Главный запуск
if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise RuntimeError("Переменная окружения BOT_TOKEN не установлена!")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Для Render: Указываем порт и путь webhook
    PORT = int(os.environ.get('PORT', 8443))
    WEBHOOK_PATH = f"/webhook/{TOKEN}"
    WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}{WEBHOOK_PATH}"

    logging.info(f"Запуск Webhook на {WEBHOOK_URL}")

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
        allowed_updates=Update.ALL_TYPES,
    )
