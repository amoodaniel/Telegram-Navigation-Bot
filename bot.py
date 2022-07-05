#!/usr/bin/env python3
import os
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler

TOKEN = os.getenv('API_KEY')

# This function replies with 'Hello <user.first_name>'
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}\n Choose your nearest Bus-stop:\n /1. effio-ette \n /2. SatelliteTown \n /3. State Housing')

#Effiote
def effiote(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}\n Here are the nearest INEC Registration centres near you, select any of them for directions:\n send 11 for INEC HQ, Highway \n send 12 for INEC State office, Marian') 

def effhigh(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}\n Here is how to get to your destination: \n 1.Board a bus/taxi going to Mobil filling station (fee: ₦50) \n 2. Drop at Mobil filling station \n 3. Board a mini-bus/taxi and tell the cab man to drop you at INEC office (fee: ₦50')

def effstate(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Directions: \n1. From effio-ette, board a bus/taxi going to marian by road safety (fee: ₦100). 2. Drop at Road safety office, locate INEC state office.')

#SatelliteTown
def sattown(update:Update, context:CallbackContext) -> None:
    update.message.reply_text(f'The Nearest PVC centre is INEC State Office, Marian Road \n Directions: \n 1. Take a keke to abang-assang junction (fee; ₦50) \n 2. From abang-assang junction, take a mini-bus/taxi to rabana roundabout (fee: ₦50) \n 3. From rabana roundabout, take a bus heading to marian by FRSC (fee: ₦50)')

#StateHousing
def statehouse(update:Update, context:CallbackContext) -> None:
    update.message.reply_text(f'The Nearest PVC centre is INEC Headquarters, Highway\nDirections:\n 1. Trek to MCC \n 2.Board a bus/taxi to mobil filling station (fee: ₦50)\n 3. Board a mini-bus/taxi and tell the cab man to drop you at INEC office (fee: ₦50)')

#Akkai Iffa
def Akkai(update:Update, context:CallbackContext) -> None:
    update.message.reply_text(f'The Nearest PVC centre is INEC State Office, Marian Road \n Directions: \n 1. Take a cab to effio-ette (fee: ₦50)\n 2.From effio-ette, board a bus/taxi going to marian by road safety (fee: ₦100)\n 3. Drop at Road safety office, locate INEC state office.')


def reply_2(update: Update, context: CallbackContext) -> None:
    text= str(update.message.text).lower()
    if text == '12':
        response = 'Directions: \n1. From effio-ette, board a bus/taxi going to marian by road safety (fee: ₦100). \n 2. Drop at Road safety office, locate INEC state office.'
    elif text == '11':
        response = 'Here is how to get to your destination: \n 1.Board a bus/taxi going to Mobil filling station (fee: ₦50) \n 2. Drop at Mobil filling station \n 3. Board a mini-bus/taxi and tell the cab man to drop you at INEC office (fee: ₦50)'
    update.message.reply_text(response)
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def random(update: Update, context: CallbackContext) -> None:
    reply_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Effio-Ette​🛣️​", callback_data='Choose a Destination\n11-INEC HQ, Higway\n12-INEC office, Marian'),
        InlineKeyboardButton("Akkai-Iffa", callback_data='Click on /4')],
        [
            InlineKeyboardButton("Satellite Town🏫", callback_data='Click on /2'),
            InlineKeyboardButton("State Housing​🏘️​", callback_data='Click on /3'),
        ]
    ])
    update.message.reply_text(
        f'Hello {update.effective_user.first_name}, Welcome to fioho bot,\nPlease choose your nearest junction, so we can direct you to a pvc centre closest to you:',
        reply_markup=reply_buttons
    )

def button(update: Update, context: CallbackContext) -> None:
    # Must call answer!
    update.callback_query.answer()
    # Remove buttons
    update.callback_query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup([])
    )
    query = update.callback_query
    update.callback_query.message.reply_text(text=update.callback_query.data)


# Insert your token here
updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))

# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_2))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

#updater.dispatcher.add_handler(CommandHandler('random', random))
updater.dispatcher.add_handler(CommandHandler('1', effiote))
updater.dispatcher.add_handler(CommandHandler('11', effhigh))
updater.dispatcher.add_handler(CommandHandler('12', effhigh))
updater.dispatcher.add_handler(CommandHandler('2', sattown))
updater.dispatcher.add_handler(CommandHandler('3', statehouse))
updater.dispatcher.add_handler(CommandHandler('4', Akkai))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('start', random))



# Connect to Telegram and wait for messages
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
