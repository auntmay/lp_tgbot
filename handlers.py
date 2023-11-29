import ephem
from datetime import date
from glob import glob
from utils import get_smile, main_keyboard, get_random_number
from random import choice


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Еще бы столько же тебя не видел {context.user_data["emoji"]}',
        reply_markup=main_keyboard())
    

def talk_to_me(update, context):
    smile = get_smile(context.user_data)
    text = update.message.text
    update.message.reply_text(f'{text} {smile}')


def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            number = int(context.args[0])
            message = get_random_number(number)
        except (ValueError, TypeError):
            message = 'ты дэбил? число введи, а не хуем по клаве бей'
    else:
        message = 'число на базу'
    update.message.reply_text(message)


def get_cat_image(update,context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))


def user_coordinates(update, context):
    coords = update.message.location
    print(coords)


def info_about_planet(update, context):
    planet = update.message.text.split(' ')[1]
    update.message.reply_text(f'Ваша планета — {planet}')

    if not hasattr(ephem, planet):
        update.message.reply_text('К сожалению, планета {planet} не найдена :(')
    else:
        object = getattr(ephem, planet)
        position = object(date.today())
        text = f'Планета {planet} сейчас находится в созвездии {str(ephem.constellation(position))}'
        update.message.reply_text(text)