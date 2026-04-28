import os
import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from dotenv import load_dotenv
from dialogflow_utils import get_dialogflow_response


load_dotenv()
TG_TOKEN = os.environ["TG_TOKEN"]
PROJECT_ID = os.environ["ID_DF"]

if not TG_TOKEN or not PROJECT_ID:
    raise ValueError("Токен и ID не заданы в .env")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level = logging.INFO)

def start(update:Update, context=CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Добрый день!'
    )

def message_handler(update:Update, context=CallbackContext):
    session_id = str(update.effective_chat.id)
    text = update.message.text
    answer, _ = get_dialogflow_response(PROJECT_ID, session_id, text)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=answer
    )


if __name__ == '__main__':
    updater = Updater(token=TG_TOKEN)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, message_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()
