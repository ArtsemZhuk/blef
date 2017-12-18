import sys
import asyncio
import telegram

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#  class BleffBotState:
    #  def __init__(self, output, keyboard):

    #  def receive_input(self, text):


class BleffBot:
    def __init__(self, token):
        # Create the EventHandler and pass it your bot's token.
        self.updater = Updater(token) 
        msg_handler = MessageHandler(Filters.text, self.msg_callback)
        start_handler = CommandHandler("start", self.start_callback, pass_args=True)
        cancel_handler = CommandHandler("end", self.cancel_callback)

        #  kicker_handler = CommandHandler("kicker", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("pair", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("pair2", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("set", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("street", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("flash", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("kare", self.kicker_callback, pass_args=True)
        #  kicker_handler = CommandHandler("flash street", self.kicker_callback, pass_args=True)
        
        self.updater.dispatcher.add_handler(msg_handler)
        self.updater.dispatcher.add_handler(start_handler)
        self.updater.dispatcher.add_handler(cancel_handler)

        self.active_chats = dict()

    def check_chat(self, chat_id):
        return chat_id in self.active_chats

    def add_chat(self, chat_id, bot):
        if not self.check_chat(chat_id):
            def output(x):
                if x:
                    bot.sendMessage(chat_id=chat_id, text=str(x))
            def keyboard(x, text):
                reply_markup = telegram.ReplyKeyboardMarkup([x], one_time_keyboard=True)
                bot.sendMessage(chat_id=chat_id, text=text, reply_markup=reply_markup)
            self.active_chats[chat_id] = PinProcedureState(output=output, keyboard=keyboard)

    def cancel_chat(self, chat_id, bot):
        if self.check_chat(chat_id):
            bot.sendMessage(chat_id=chat_id, text='Bye!')
            del self.active_chats[chat_id]

    def msg_callback(self, bot, update):
        chat_id = update.message.chat_id
        if self.check_chat(chat_id):
            if update.message.text.lower().startswith('кто такой'):
                bot.sendMessage(chat_id=chat_id, text='Oleg Tinkov is a Russian entrepreneur and cycling sponsor. According to Forbes, in 2014 he was ranked 1210 in the list of the wealthiest people in the world, on the list of the richest businessmen in ...')
            elif update.message.text.lower().startswith('как тебя'):
                bot.sendMessage(chat_id=chat_id, text='Меня зовут бот пин-процердурщик. Готов ответить на ваши вопросы.')
            else:
                self.active_chats[chat_id].receive_input(update.message.text)

    def start_callback(self, bot, update, args):
        chat_id = update.message.chat_id
        bot.sendMessage(chat_id=chat_id, text="huesos")
        chat_id = update.message.chat_id
        self.add_chat(chat_id, bot)

    def cancel_callback(self, bot, update):
        chat_id = update.message.chat_id
        self.cancel_chat(chat_id, bot)

    def start(self):
        # Start the Bot
        self.updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()



if __name__ == '__main__':
    bleff_bot = BleffBot()
    bleff_bot.start()
