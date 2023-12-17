# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:51:49 2023

@author: Raydesel
"""

import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from jokeapi import Jokes
import asyncio

async def get_joke_category(category):
    j = await Jokes()
    joke = await j.get_joke(category=[category])
    return format_joke(joke)

def format_joke(joke):
    if joke["type"] == "single":
        return joke["joke"]
    else:
        return f"{joke['setup']}\n{joke['delivery']}"

TOKEN = '<Token>'

COMMANDS = {
    'programming': get_joke_category,
    'christmas': get_joke_category,
    'misc': get_joke_category,
    'dark': get_joke_category,
    'pun': get_joke_category,
    'spooky': get_joke_category,
    'help': lambda: "Select from the following joke types: 'programming', 'christmas', 'misc', 'dark', 'pun', 'spooky'.",
}

keys = [[KeyboardButton(text=text)] for text in COMMANDS]
KEYBOARD = ReplyKeyboardMarkup(keyboard=keys)

class MarketingBot(telepot.helper.ChatHandler):
    def open(self, initial_msg, seed):
        self.sender.sendMessage(COMMANDS["help"](), reply_markup=KEYBOARD)
        return True

    def on_chat_message(self, msg):
        content_type, _, _ = telepot.glance(msg)

        if content_type != 'text':
            self.sender.sendMessage("I don't understand you. Please type 'help' for options", reply_markup=KEYBOARD)
            return

        command = msg['text'].lower()
        if command not in COMMANDS:
            self.sender.sendMessage("I don't understand you. Please type 'help' for options", reply_markup=KEYBOARD)
            return

        if command in ['programming', 'christmas', 'misc', 'dark', 'pun', 'spooky']:
            # For category commands, send a message to get the joke for that category
            joke = asyncio.run(COMMANDS[command](command))
            self.sender.sendMessage(joke, reply_markup=KEYBOARD)
        else:
            # For other commands, execute the command directly
            message = COMMANDS[command]()
            self.sender.sendMessage(message, reply_markup=KEYBOARD)

    def on_idle(self, event):
        self.close()

    def on_close(self, event):
        pass

# Create and start the bot
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MarketingBot, timeout=10),
])
MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
