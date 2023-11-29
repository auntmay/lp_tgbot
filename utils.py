import settings
from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from random import choice, randint


def main_keyboard():
    return ReplyKeyboardMarkup([['/cat', KeyboardButton('хде я?', request_location=True)]])


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def get_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'иди нахуй, чепушила. Нахуя ты победил? {user_number} больше, чем {bot_number}'
    elif user_number == bot_number:
        message = f'на тоненького. ничья'
    else: 
        message = f'потеряйся, петушок. Я подебил'
    return message

