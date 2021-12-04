from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters
from tfidf import choose_answer


updater = Updater(token="epic_token")
dispatcher = updater.dispatcher


# Приветствие
def start(update: Update, context: CallbackContext):
    update.message.reply_text('''
    Здравствуйте! Я попытаюсь ответить на ваши всевозможные вопросы, связанные с волонтёрством в Кронодском заповеднике.
    Пишите, как вам удобно, но если я отвечу неправильно, то попробуйте переформулировать сообщение.
    Спасибо, и надеюсь, что я вам помогу!
    ''')


# Ответ на сообщение
def answer(update: Update, context: CallbackContext):
    answer = choose_answer(update.message.text)
    update.message.reply_text(answer)


answer_handler = MessageHandler(Filters.text, answer)
start_handler = CommandHandler("start", start)

dispatcher.add_handler(answer_handler)
dispatcher.add_handler(start_handler)


updater.start_polling()