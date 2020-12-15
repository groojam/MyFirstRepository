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
import Micro_Dust # 미세먼지 API 파이썬 파일
import PMS7003 # 미세먼지 센서 값 가져오는 파이썬 파일
import StepMotor # 모터를 제어하는 파이썬 파일
import Relay # 릴레이로 공기청정기 및 제습기를 제어하는 파이썬 파일

import serial
import struct
import time
import Adafruit_DHT

import logging

import RPi.GPIO as GPIO
import time
from collections import deque

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
    update.message.reply_text('집에서 측정한 온도, 습도, 미세먼지 측정값입니다.')
    update.message.reply_text('온도={0:0.1f}*C  습도={1:0.1f}% \n'.format(temperature, humidity))
    update.message.reply_text('미세먼지(PM10)농도 : %s\n초미세먼지(PM2.5)농도 : %s' % (dusts[2],dusts[1]))

def MicroDust(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    md = Micro_Dust.MicroDust()
    update.message.reply_text('인천 미추홀구에 있는 관측소에서 측정한 외부의 미세먼지 측정값입니다.')
    update.message.reply_text('미세먼지(PM10)농도 : {0}\n초미세먼지(PM2.5)농도 : {1}'.format(md[0],md[1]))

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('/now를 입력하시면 센서 값이 전송됩니다!\n\n' +
                              '/MicroDust를 입력하시면 인천 미추홀의 미세먼지 정보가 전송됩니다!\n\n' +
                              '/winopen을 입력하시면 창문이 열립니다!\n\n' +
                              '/winclose를 입력하시면 창문이 닫힙니다!\n\n' +
                              '/airon을 입력하시면 공기청정기가 작동됩니다!\n\n' +
                              '/airoff를 입력하시면 공기청정기의 작동이 멈춥니다!\n\n' +
                              '/dehumidon을 입력하시면 제습기가 작동됩니다!\n\n' +
                              '/dehumidoff를 입력하시면 제습기의 작동이 멈춥니다!')

def WinOpen(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('창문을 열겠습니다.')
    StepMotor.window('open')
    update.message.reply_text('창문이 열렸습니다!')

def WinClose(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('창문을 닫겠습니다.')
    StepMotor.window('close')
    update.message.reply_text('창문이 닫혔습니다!')

def AirOff(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('공기청정기 작동을 멈춤니다.')
    Relay.relay(1, 1)
    update.message.reply_text('공기청정기가 작동이 멈췄습니다!')

def AirOn(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('공기청정기를 작동시킵니다.')
    Relay.relay(1, 0)
    update.message.reply_text('공기청정기 작동이 되었습니다!')

def DehumidOff(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('제습기 작동을 멈춤니다.')
    Relay.relay(2, 1)
    update.message.reply_text('제습기가 작동이 멈췄습니다!')

def DehumidOn(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('제습기를 작동시킵니다.')
    Relay.relay(2, 0)
    update.message.reply_text('제습기 작동되었습니다!')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1217163377:AAEfbmfoPU-T6awKI9ZBR3X3wBLSrYn-j8s", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("now", now)) # 집에서 측정한 온도, 습도, 미세먼지 측정값
    dispatcher.add_handler(CommandHandler("MicroDust", MicroDust)) # 인천 미추홀구에 있는 관측소에서 측정한 외부의 미세먼지 측정값
    dispatcher.add_handler(CommandHandler("winopen", WinOpen)) # 창문을 연다.
    dispatcher.add_handler(CommandHandler("winclose", WinClose)) # 창문을 닫는다.
    dispatcher.add_handler(CommandHandler("airon", AirOn)) # 공기청정기를 작동시킨다.
    dispatcher.add_handler(CommandHandler("airoff", AirOff)) # 공기청정기의 작동을 멈춘다.
    dispatcher.add_handler(CommandHandler("dehumidon", DehumidOn)) # 제습기를 작동시킨다.
    dispatcher.add_handler(CommandHandler("dehumidoff", DehumidOff)) # 제습기의 작동을 멈춘다.
    dispatcher.add_handler(CommandHandler("help", help_command)) # 명령어들에 대한 도움말을 제공합니다.

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
