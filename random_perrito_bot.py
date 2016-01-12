# random_perrito_bot.py
# Israel Zuñiga de la Mora | 2016

# Import required modules to playground
import os, telebot, logging, numpy

# Setup the logger
logging.basicConfig(filename='bot.log', level=logging.CRITICAL)

# Load from environment the key for Telegram's API
random_perrito = telebot.AsyncTeleBot(os.environ['RANDOM_PERRITO_BOT_KEY'])

# Message handler for start and help commands
@random_perrito.message_handler(commands=['start'])
def help_command(message):
    random_perrito.reply_to(message,"""\
    Hey there! Are you ready for the magic?
    Send /random to obtain a random number. You can request without limits!
    Available commands: /start, /random and /about
    """)

# Message handler for about command
@random_perrito.message_handler(commands=['about'])
def about_command(message):
    random_perrito.reply_to(message,"""\
    About this bot and the numbers.
    The results are random samples from a normal (Gaussian) distribution. You can learn more about it here: https://en.wikipedia.org/wiki/Normal_distribution
    Random Perrito is a Telegram Bot. You can see the source code at:
    http://github.com/israelzuniga/random-perrito-bot/
    Author: Israel Zúñiga de la Mora @israelzuniga
    """)

# Message handler for random command
# Here be dragons
@random_perrito.message_handler(commands=['random'])
def random_command(message):
    magic_number = str(numpy.random.normal(0.1, 99999))
    random_perrito.reply_to(message, magic_number)
    print('Command response: ' + magic_number)

# Listener to save received mesages
def console_listener(messages):
    for message in messages:
        '''
        To have a message listener is to have a Single Point OF Failure(SPOF)
        So, we must handle exceptions for failure. In case of any expected
        action, command or Unicode character our app doesn't support.
        Without error handling our bot can stop working and we could enter
        to an infinite loop using nohup
        '''
        try:
            # Print the good stuff on the console
            print('[Sender ID: ' + str(message.chat.id) + '] Text: ' + message.text)
        except:
            # Ignore errors at printing the messages
            pass

random_perrito.set_update_listener(console_listener)
random_perrito.polling()
