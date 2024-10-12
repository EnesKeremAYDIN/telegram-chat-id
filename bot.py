import os
from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()
telegram_bot_key = os.getenv('TELEGRAM_BOT_KEY')

async def get_chat_and_topic_id(update: Update, context) -> None:
    chat_id = update.message.chat_id
    topic_id = update.message.message_thread_id if update.message.message_thread_id else "Bu mesaj bir topic'e ait değil."
    await update.message.reply_text(f"Kanal ID'si: {chat_id}\nTopic ID'si: {topic_id}")

def main() -> None:
    application = Application.builder().token(telegram_bot_key).build()
    application.add_handler(CommandHandler("get_chat_id", get_chat_and_topic_id))
    application.run_polling()

if __name__ == '__main__':
    main()
