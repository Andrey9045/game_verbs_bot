import os
import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from google.cloud import dialogflow
from dotenv import load_dotenv


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

def detect_intent_texts(update:Update, context=CallbackContext, project_id='exalted-ability-494118-b0'):
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, update.effective_chat.id)
        text_input = dialogflow.TextInput(
            text=update.message.text,
            language_code='ru'
        )
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response.query_result.fulfillment_text
        )
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения от {update.effective_chat.id}:{e}")
        update.message.reply_text(f"Извините, произошла ошибка: {e}")


if __name__ == '__main__':
    updater = Updater(token=TG_TOKEN)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()
