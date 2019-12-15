# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:36:36 2019

@author: saura
"""


import requests
import time
import schedule

def telegram_bot_sendtext(bot_message):
    bot_token='944323355:AAGhMoNlzlNwx7Y0Y2HMEFSG4HF7Grzz7Qw'
    bot_chatID='811375934'
    send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response=requests.get(send_text)
    return response.json()
test=telegram_bot_sendtext("Testing bot")
print(test)


def report():
    my_balance=10
    my_message = "Current balance is: {}".format(my_balance)   ## Customize your message
    telegram_bot_sendtext(my_message)
    
schedule.every().day.at("10:30").do(report)


while True:
    schedule.run_pending()
    time.sleep(1)