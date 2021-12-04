from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters
from tfidf import choose_answer

updater = Updater(token="epic_token")
dispatcher = updater.dispatcher

def echo(update: Update, context: CallbackContext):
    answer = choose_answer(update.message.text)
    update.message.reply_text(answer)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
