from slackbot.bot import respond_to
from gsearch.googlesearch import search
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply("hi")
    message.react('+1')

@respond_to('Give me (.*)')
def giveme(message, term):
    message.reply('Here is {}'.format(term))
    
