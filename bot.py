import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8690887958:AAEHfy8T9gH1Tc4sQnI1MDvbr8zo2oXMjfc"

total_in = 0
total_out = 0

def start(update, context):
    update.message.reply_text("Balance Bot Online ✅")

def check_payment(update, context):
    global total_in

    text = update.message.text.lower()

    # amount detect
    match = re.search(r'\$?(\d+(\.\d+)?)', text)

    if "received" in text and match:
        amount = float(match.group(1))
        total_in += amount

        update.message.reply_text(
            f"🟢 Payment Received\n\n"
            f"Amount: ${amount}\n"
            f"➕ Total In: ${total_in}\n"
            f"➖ Total Out: ${total_out}"
        )

def add_out(update, context):
    global total_out

    amount = float(context.args[0])
    total_out += amount

    update.message.reply_text(
        f"🔴 Payment Sent\n\n"
        f"Amount: ${amount}\n"
        f"➕ Total In: ${total_in}\n"
        f"➖ Total Out: ${total_out}"
    )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("out", add_out))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_payment))

updater.start_polling()
updater.idle()
