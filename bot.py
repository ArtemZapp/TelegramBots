import config
import telebot

bot = telebot.TeleBot(config.token)
print(bot.get_me())