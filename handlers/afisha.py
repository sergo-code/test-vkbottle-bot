from vkbottle.bot import BotLabeler, rules
from vkbottle.bot import Message

from keyboards import poster_menu
from services.afisha import get_afisha
from utils.sql import check_user


afisha_labeler = BotLabeler()
afisha_labeler.vbml_ignore_case = True
afisha_labeler.auto_rules = [rules.PeerRule(from_chat=False)]


@afisha_labeler.message(text='Афиша')
async def afisha(message: Message):
    await message.answer(f"На какой день Вас интересует афиша?", keyboard=poster_menu)


@afisha_labeler.message(payload={'cmd': 'afisha_today'})
async def afisha(message: Message):
    afisha = get_afisha(check_user(message.from_id)[0], 'today')
    if afisha:
        text = str()
        for item in afisha:
            text += f"{item['name']}\n{item['price']}\n{item['link']}\n"
        await message.answer(text)
    else:
        await message.answer('Сегодня нет доступных мероприятий')


@afisha_labeler.message(payload={'cmd': 'afisha_tomorrow'})
async def afisha(message: Message):
    afisha = get_afisha(check_user(message.from_id)[0], 'tomorrow')
    if afisha:
        text = str()
        for item in afisha:
            text += f"{item['name']}\n{item['price']}\n{item['link']}\n"
        await message.answer(text)
    else:
        await message.answer('Завтра нет доступных мероприятий')
