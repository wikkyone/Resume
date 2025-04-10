import telebot

with open('config.txt') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)