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
    city = check_user(message.from_id)[0]
    weather = await get_weather(city, 'today')
    text = f'Погода [{city}]\n\n'
    for item in weather:
        text += f"&#8986; - - - - - {item['time']} - - - - -\n" \
                f"&#127777; {item['temperature']}\n" \
                f"&#128221; {item['description']}\n\n"

    await message.answer(text)


@weather_labeler.message(payload={'cmd': 'weather_tomorrow'})
async def weather(message: Message):
    city = check_user(message.from_id)[0]
    weather = await get_weather(city, 'tomorrow')
    text = f'Погода [{city}]\n\n'
    for item in weather:
        text += f"&#8986; - - - - - {item['time']} - - - - -\n" \
                f"&#127777; {item['temperature']}\n" \
                f"&#128221; {item['description']}\n\n"

    await message.answer(text)
