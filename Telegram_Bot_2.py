import telebot
import random
from telebot import types
with open('config_2.txt') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)
secret_number = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global secret_number
    secret_number = random.randint(1, 100)
    bot.send_message(message.chat.id, "Я загадал число от 1 до 100. Попробуй угадать!")

@bot.message_handler(func=lambda message: message.text.isdigit())
def get_number(message):
    global secret_number
    
    if secret_number is None:
        bot.send_message(message.chat.id, "Сначала напишите /start")
        return
    
    user_number = int(message.text)
    
    if user_number < secret_number:
        bot.send_message(message.chat.id, "Загаданное число больше")
    elif user_number > secret_number:
        bot.send_message(message.chat.id, "Загаданное число меньше")
    else:
        bot.send_message(message.chat.id, "Вы угадали число! Чтобы начать заново, напишите /start")
        secret_number = None

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
