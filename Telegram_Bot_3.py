import telebot
import requests
from telebot import types

with open('config_3.txt') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

with open('config_weather.txt') as f:
    weather_token = f.read().strip()

WEATHER_API_KEY = weather_token

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},ru&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data.get('cod') != 200:
        return None
    main = data.get('main')
    weather = data.get('weather')[0]
    temperature = main.get('temp')
    description = weather.get('description')
    return temperature, description

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    cities = ['Moscow', 'Saint Petersburg', 'Kazan']
    buttons = [types.KeyboardButton(city) for city in cities]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Привет! Я могу рассказать тебе погоду в Москве, Санкт-Петербурге и Казани.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Moscow', 'Saint Petersburg', 'Kazan'])
def handle_city_weather(message):
    city = message.text
    weather_data = get_weather(city)
    if weather_data:
        temperature, description = weather_data
        response = f'Погода в {city}: {temperature}°C, {description}'
    else:
        response = 'Произошла ошибка при получении данных о погоде.'
    bot.send_message(message.chat.id, response)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    print("Бот запущен...")
