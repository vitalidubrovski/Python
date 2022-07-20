from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import create_db as cr

a = '5566223749:AAGvjGHm8PfmZ5L1rFUyCFpE1z0fBlFITZg'
updater = Updater(
    token=a, use_context=True)
dispatcher = updater.dispatcher
bot = Bot(token=a)


name_it = ''
surname_it = ''
number_it = ''
email_it = ''

NAME = 0
SURNAME = 1
PHONE = 2
EMAIL = 3
MAIN = 4
MESSAGE = 5


def start(update, context):
    context.bot.send_message(
        update.effective_chat.id, f'Привет!\nВ любой непонятной ситуации введи\nкоманду: /main')

    return MAIN


def main(update, context):
    global message
    message = update.message.text
    if message.lower() == '/main':
        context.bot.send_message(
            update.effective_chat.id, f'Выбери пункт меню, введя соответствующую команду: \n/1 - Показать все записи.\n/2 - Добавить новую запись.')
        cr.init_data_base('base_phone.csv')

        return MESSAGE

    elif message == '/1':
        context.bot.send_message(update.effective_chat.id, f'{cr.retrive()}')

    elif message == '/2':
        context.bot.send_message(update.effective_chat.id, f'Введите имя')

        return NAME


def get_name(update, context):
    global name_it
    name_it = update.message.text
    context.bot.send_message(update.effective_chat.id, f'Введите фамилию')

    return SURNAME


def get_surname(update, context):
    global surname_it
    surname_it = update.message.text
    context.bot.send_message(update.effective_chat.id,
                             f'Введите номер телефона')

    return PHONE


def get_number(update, context):
    global number_it
    number_it = update.message.text
    context.bot.send_message(update.effective_chat.id,
                             f'Введите электронную почту')

    return EMAIL


def get_email(update, context):
    global email_it
    email_it = update.message.text
    cr.create(name_it, surname_it, number_it, email_it)
    context.bot.send_message(update.effective_chat.id,
                             f'Контакт успешно добавлен!')

    return ConversationHandler.END


def cancel(update, context):
    ConversationHandler.END


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
main_handler = CommandHandler('main', main)
main_message_handler = MessageHandler(Filters.text, main)
get_name_handler = MessageHandler(Filters.text, get_name)
get_surname_handler = MessageHandler(Filters.text, get_surname)
get_number_handler = MessageHandler(Filters.text, get_number)
get_email_hendler = MessageHandler(Filters.text, get_email)
cancel_hendler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
    MAIN: [main_handler],
    MESSAGE: [main_message_handler],
    NAME: [get_name_handler],
    SURNAME: [get_surname_handler],
    PHONE: [get_number_handler],
    EMAIL: [get_email_hendler]
},
    fallbacks=[cancel_hendler])

dispatcher.add_handler(conv_handler)
print('server start')
updater.start_polling()
updater.idle()
