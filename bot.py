import settings, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice, randint
from handlers import (greet_user, guess_number, info_about_planet, 
                      get_cat_image, user_coordinates, talk_to_me)


logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('planet', info_about_planet))
    dp.add_handler(CommandHandler('cat', get_cat_image))
    dp.add_handler(MessageHandler(Filters.regex('^(кто миукает?)$'), get_cat_image))     
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))     
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
