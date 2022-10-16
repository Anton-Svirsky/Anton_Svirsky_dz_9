from telegram import Update
from telegram.ext import Updater, CommandHandler, callbackcontext
from bot_commands import *

updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('calculation', calculation_command))

print('server start')
updater.start_polling()
updater.idle()