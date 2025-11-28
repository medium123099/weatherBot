import telebot
import requests
import json
bot = telebot.TeleBot(token='token')
API='tokenweathermap'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Привет,введите название города!")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru')
    if res.status_code==200:
        data=json.loads(res.text)
        temp=data['main']['temp']
        description=data['weather'][0]['description']
        if temp==1:
            temperatura='градус'
        elif 2<=temp<5:
            temperatura='градуса'
        else:
            temperatura='градусов'
        bot.reply_to(message,f'Сейчас погода:{int(temp)}° {temperatura}\n{description} ☁️')
    else:
        bot.reply_to(message,"Город указан не верно!Введите корректное название города!")
bot.polling(none_stop=True)