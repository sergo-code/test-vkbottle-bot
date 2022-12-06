from vkbottle.bot import BotLabeler, rules
from vkbottle.bot import Message

from keyboards import weather_menu
from services.weather import get_weather
from utils.sql import check_user


weather_labeler = BotLabeler()
weather_labeler.vbml_ignore_case = True
weather_labeler.auto_rules = [rules.PeerRule(from_chat=False)]


@weather_labeler.message(text='Погода')
async def weather(message: Message):
    await message.answer(f"На какой день Вас интересует погода?", keyboard=weather_menu)


@weather_labeler.message(payload={'cmd': 'weather_today'})
async def weather(message: Message):
    weather = get_weather(check_user(message.from_id)[0])
    text = f"Сейчас: {weather['temp']}\n" \
           f"Ощущается: {weather['temp_min']}\n" \
           f"Максимальная температура: {weather['temp_max']}\n" \
           f"Минимальная температура: {weather['temp_min']}\n"
    await message.answer(text)


@weather_labeler.message(payload={'cmd': 'weather_tomorrow'})
async def weather(message: Message):
    await message.answer(f"Погода завтра")
