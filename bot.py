try:
    import imghdr
except:
    pass

import telegram
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8690887958:AAEHfy8T9gH1Tc4sQnI1MDvbr8zo2oXMjfc"

balance = 0

def handle_message(update, context):
    global balance
    text = update.message.text
    
    if "received" in text.lower():
        words = text.split()
        for w in words:
            if w.replace("$","").isdigit():
                amount = int(w.replace("$",""))
                balance += amount
                update.message.reply_text(f"Total Balance: ${balance}")

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(MessageHandler(filters.Text, handle_message))

updater.start_polling()
updater.idle()
