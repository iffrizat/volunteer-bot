from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, CommandHandler, Filters
from tfidf import choose_answer


updater = Updater(token="epic_token")
dispatcher = updater.dispatcher


# Приветствие
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Здравствуйте! Я попытаюсь ответить на ваши всевозможные вопросы, связанные с волонтёрством в Кронодском заповеднике.\n\nПишите, как вам удобно, но если я отвечу неправильно, то попробуйте переформулировать сообщение.\n\nСпасибо, и надеюсь, что я вам помогу.")


# Ответ на сообщение
def answer(update: Update, context: CallbackContext):
    answer = choose_answer(update.message.text)
    update.message.reply_text(answer)


start_handler = CommandHandler("start", start)
answer_handler = MessageHandler(Filters.text, answer)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)


updater.start_polling()