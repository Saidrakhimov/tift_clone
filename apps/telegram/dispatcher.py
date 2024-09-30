from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler, ConversationHandler
from apps.telegram.handlers import commands, common, registration
from apps.telegram import States
from apps.telegram import States
from apps.telegram.handlers.registration import start

BOT_TOKEN = "6402922799:AAFgUO_Wv_GFcqkRquFCAbZiSiaFW2yYXW4"
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(
    ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            States.PHONE: [MessageHandler(Filters.all, registration.get_phone)],
            States.FULL_NAME: [MessageHandler(Filters.all, registration.get_first_name)],
            States.PASSPORT: [MessageHandler(Filters.all, registration.get_passport)],
            States.PINFL: [MessageHandler(Filters.all, registration.get_pinfi)],
            States.GENDER: [MessageHandler(Filters.text, registration.get_gender)],
            States.BIRTH_DATE: [MessageHandler(Filters.text, registration.get_birth_date)],
        },
        fallbacks=[
            CommandHandler("cancel", registration.fallback),
            MessageHandler(Filters.all, registration.fallback)
        ]
    )
)
