import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level = logging.INFO)


def start(update: Update, context = CallbackContext):
	context.bot.send_message(chat_id=update.effective_chat.id, text ='Добрый день!')

def echo(update: Update, context = CallbackContext):
	context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.text)

updater =  Updater(token = '8700138650:AAEuBP8lq01c_qEQRq_rYRU04Cfh8Q63a-Y')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
updater.start_polling()
updater.idle()
