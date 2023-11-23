import settings, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')


def greet_user(update, context):
    print(update)
    update.message.reply_text('Спасибо нахуй!')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
