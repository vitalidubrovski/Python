from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import calc as c
a = '5566223749:AAGvjGHm8PfmZ5L1rFUyCFpE1z0fBlFITZg'
bot = Bot(token=a)
updater = Updater(
    token=a, use_context=True)
dispatcher = updater.dispatcher


START = 0
CONTINUE1 = 1
CONTINUE2 = 2
RESULT = 3
OFF = 4


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Введи действительную часть первого числа: ')

    return START


def input_real_c1(update, context):
    global real_num1
    real_num1 = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введи мнимую часть первого числа: ')

    return CONTINUE1

def input_image_c1(update, context):
    global image_num1
    image_num1 = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введи действительную часть второго числа: ')

    return CONTINUE2

def input_real_c2(update, context):
    global real_num2
    real_num2 = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Введи мнимую часть второго числа: ')

    return RESULT

def input_image_c2(update, context):
    global image_num2
    image_num2 = update.message.text
    context.bot.send_message(update.effective_chat.id,
                             'Введи действие "/", "*", "-", "+" ')

    return OFF

def operations(update, context):
    oper = update.message.text
    result = 0
    if oper == '+':
        result = c.sum(complex(float(real_num1), float(image_num1)), complex(float(real_num2), float(image_num2)))
    elif oper == '-':
        result = c.sub(complex(float(real_num1), float(image_num1)), complex(float(real_num2), float(image_num2)))
    elif oper == '*':
        result = c.mult(complex(float(real_num1), float(image_num1)), complex(float(real_num2), float(image_num2)))
    elif oper == '/' and (float(real_num2), float(image_num2)!=0):
        result = c.div(complex(float(real_num1), float(image_num1)), complex(float(real_num2), float(image_num2)))
    else:
        context.bot.send_message(update.effective_chat.id,'Ошибка деления на 0')
    context.bot.send_message(update.effective_chat.id,f'Результат: {oper} => {result}')


    return ConversationHandler.END



def cancel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
real_handler_1 = MessageHandler(Filters.text, input_real_c1)
image_handler_1 = MessageHandler(Filters.text, input_image_c1)
real_handler_2 = MessageHandler(Filters.text, input_real_c2)
image_handler_2 = MessageHandler(Filters.text, input_image_c2)
result_handler = MessageHandler(Filters.text, operations)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                    START:[real_handler_1],
                                    CONTINUE1:[image_handler_1],
                                    CONTINUE2:[real_handler_2],
                                    RESULT: [image_handler_2],
                                    OFF: [result_handler]
                                   },
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

print('start server')
updater.start_polling()
updater.idle()
