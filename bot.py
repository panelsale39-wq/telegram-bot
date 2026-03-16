import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("8690887958:AAEHfy8T9gH1Tc4sQnI1MDvbr8zo2oXMjfc")

balance_in = 0
balance_out = 0

def start(update, context):
    update.message.reply_text("Bot chal raha hai ✅")

def add(update, context):
    global balance_in
    amount = int(context.args[0])
    balance_in += amount
    update.message.reply_text(f"You received ${amount}\nTotal In: ${balance_in}")

def out(update, context):
    global balance_out
    amount = int(context.args[0])
    balance_out += amount
    update.message.reply_text(f"You sent ${amount}\nTotal Out: ${balance_out}")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("add", add))
dp.add_handler(CommandHandler("out", out))

updater.start_polling()
updater.idle()
