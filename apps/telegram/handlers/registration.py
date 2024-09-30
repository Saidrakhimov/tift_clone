from telegram.ext import ConversationHandler

from apps.telegram.keyboards import replies
from apps.telegram import States
from apps.telegram.models import TelegramModel
from apps.telegram.keyboards.replies import get_contact_button
from telegram import ReplyKeyboardRemove
from apps.education.models import Faculty
from apps.common.models import Region


def start(update, context):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name
    telegram_id = user.id

    TelegramModel.objects.update_or_create(
        telegram_id=telegram_id,
        defaults={
            "first_name": first_name,
            "last_name": last_name
        }
    )
    message = "Assalomaleylum TIFT.uz botiga xush kelipsiz ariza yuborish uchun telefon raqmingizni yuboring"
    update.message.reply_text(message, reply_markup=get_contact_button())
    return States.PHONE


def get_phone(update, context):
    print("Update in phone state ")
    if update.message and update.message.contact:
        contact_user_id = update.message.contact.user_id
        user_id = update.message.from_user.id
        if contact_user_id != user_id:
            update.message.reply_text("Iltmos ozingizni kantaktingizni kiriting Bu sizniki emas!")
            return States.PHONE
        else:
            phone = update.message.contact.phone_number
            context.user_data['phone_number'] = phone
            update.message.reply_text("Iltmos ismingizni kiritng", reply_markup=ReplyKeyboardRemove())
            return States.FULL_NAME
    else:
        update.message.reply_text("Iltmos telefon raqamingizni yuboring", reply_markup=replies.get_contact_button())
        return States.PHONE


def get_first_name(update, context):
    if update.message and update.message.text:
        full_name = update.message.text
        context.user_data['full_name'] = full_name
        update.message.reply_text("every think is okey please send your passport in AA1234567 format",
                                  reply_markup=ReplyKeyboardRemove())
        return States.PASSPORT
    update.message.reply_text("please send your name as text", reply_markup=ReplyKeyboardRemove())
    return States.FULL_NAME


import re


def get_passport(update, context):
    if update.message and update.message.text:
        if not re.match("^[A-Z]{2}\d{7}$", update.message.text):
            update.message.reply_text("Please send your passport data in AA1234567 format",
                                      reply_markup=ReplyKeyboardRemove())
            return States.PASSPORT
        context.user_data['passport'] = update.message.text
        update.message.reply_text("Correct please send you PINFl")
        return States.PINFL

    update.message.reply_text("please send you passport data as text")
    return States.PASSPORT


def get_pinfi(update, context):
    if update.message and update.message.text:
        text = update.message.text
        if str(text).isdigit() and len(text) == 14:
            context.user_data['pinfl'] = text
            update.message.reply_text("Please Choose you gender", reply_markup=replies.get_gender_button())
            return States.GENDER
        update.message.reply_text("Please send your correct PINFL")
        return States.PINFL


def get_gender(update, context):
    if update.message and update.message.text:
        text = update.message.text
        genders = {
            "Erkak": "male",
            "Ayol": "female"
        }
        if text in genders.keys():
            context.user_data['gender'] = genders[text]
            update.message.reply_text("Tugilgan sanangizni 01.01.2000 formatida yuboring",
                                      reply_markup=ReplyKeyboardRemove())
            return States.BIRTH_DATE

    update.message.reply_text("Please choose you gender through the button bellow",
                              reply_markup=replies.get_gender_button())
    return States.GENDER


from datetime import datetime


def get_birth_date(update, context):
    if update.message and update.message.text:
        text = update.message.text
        if re.match("^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(199[6-9]|20[0-9]{2})$", text):
            try:
                birth_date = datetime.strptime(text, "%d.%m.%Y")
                context.user_data['birth_date'] = birth_date

                TelegramModel.objects.create(
                    name=name
                    
                )

                update.message.reply_text("Please, choose your faculy",
                                          reply_markup=replies.get_items(Faculty.objects.all(), "title"))
                return ConversationHandler.END

            except ValueError:
                pass
    update.message.reply_text("Please send you birht date in 01.01 format. Year should be greater than 1995")
    return States.BIRTH_DATE




def cancel(update, context):
    update.message.reply_text("Suhbat bekor qilindi.")
    return ConversationHandler.END