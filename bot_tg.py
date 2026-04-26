import os
import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from google.cloud import dialogflow
from dotenv import load_dotenv


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level = logging.INFO)

def start(update:Update, context=CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Добрый день!'
    )

def detect_intent_texts(update:Update, context=CallbackContext, project_id='exalted-ability-494118-b0'):
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


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    updater = Updater(token=tg_token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, detect_intent_texts)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()
