from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters

updater = Updater(token="epic_token")
dispatcher = updater.dispatcher

# Простое повторение сообщения
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()