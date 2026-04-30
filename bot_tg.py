import os
import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from dotenv import load_dotenv
from dialogflow_utils import get_dialogflow_response


logger = logging.getLogger(__name__)

def start(update:Update, context=CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Добрый день!'
    )

def message_handler(update:Update, context=CallbackContext):
    user_id = update.effective_chat.id
    logger.debug(f"Сообщение пользователя {user_id}: {update.message.text}")
    try:
        session_id = f"tg-{user_id}"
        text = update.message.text
        answer, _ = get_dialogflow_response(project_id, session_id, text)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=answer
        )
    except Exception as e:
        logger.exception(f"Ошибка при обработке сообщения пользователя {user_id}:{ e}")
        update.message.reply_text("Извините, произошла ошибка")


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    project_id = os.environ["ID_DF"]   
    if not tg_token or not project_id:
        raise ValueError("Токен и ID не заданы в .env")
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)
    updater = Updater(token=tg_token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, message_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()
