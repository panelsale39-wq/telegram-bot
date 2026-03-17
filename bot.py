import telegram
from telegram.ext import Updater, MessageHandler, filters

TOKEN = "8690887958:AAEHfy8T9gH1Tc4sQnI1MDvbr8zo2oXMjfc"

def reply(update, context):
    text = update.message.text
    update.message.reply_text("Aap ne likha: " + text)

updater = Updater(TOKEN)

dp = updater.dispatcher
dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

updater.start_polling()
updater.idle()
