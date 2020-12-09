#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import Micro_Dust

import serial
import struct
import time
import Adafruit_DHT
import PMS7003

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def now(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('온도={0:0.1f}*C  습도={1:0.1f}% \n'.format(temperature, humidity))
    update.message.reply_text('미세먼지\n PM 1.0 : %s, PM 2.5 : %s, PM 10.0 : %s' % (dusts[0],dusts[1],dusts[2]))

def MicroDust(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    md = Micro_Dust.MicroDust()
    update.message.reply_text('시간: {0}\n미세먼지(PM10)농도 : {1}\n미세먼지(PM2.5)농도 : {2}'.format(md[0],md[1],md[2]))

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('/now를 입력하시면 센서 값이 전송됩니다!\n/MicroDust를 입력하시면 인천 미추홀의 미세먼지 정보가 전송됩니다!')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1420071822:AAHAiYgY0LDXa3lgaPv8b7WOM0AolAV4RPY", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("now", now))
    dispatcher.add_handler(CommandHandler("MicroDust", MicroDust))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

# UART / USB Serial : 'dmesg | grep ttyUSB'
USB0 = '/dev/ttyUSB0'
UART = '/dev/ttyAMA0'

# USE PORT
SERIAL_PORT = USB0

# Baud Rate
Speed = 9600

if __name__ == '__main__':
    #serial setting 
    ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)

    dust = PMS7003.PMS7003()

    while True:
        ser.flushInput()
        buffer = ser.read(1024)

        sensor = Adafruit_DHT.DHT11
        pin = 17
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')

        if(dust.protocol_chk(buffer)):
            print("DATA read success")

            # print data
            dust.print_serial(buffer)

            #get dust data
            dusts = dust.get_data(buffer)
            print(dusts)

        else:
            print("DATA read fail...")
        main()
    ser.close()
