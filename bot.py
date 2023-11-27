import settings, logging, ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
from datetime import date
from glob import glob
from random import choice, randint
from emoji import emojize


logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Еще бы столько же тебя не видел {context.user_data["emoji"]}')


def talk_to_me(update, context):
    smile = get_smile(context.user_data)
    text = update.message.text
    update.message.reply_text(f'{text} {smile}')


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


def get_cat_image(update,context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('planet', info_about_planet))
    dp.add_handler(CommandHandler('cat', get_cat_image))     
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
