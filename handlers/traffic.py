from vkbottle.bot import BotLabeler, rules
from vkbottle.bot import Message

from services.traffic import get_traffic
from utils.sql import check_user

traffic_labeler = BotLabeler()
traffic_labeler.vbml_ignore_case = True
traffic_labeler.auto_rules = [rules.PeerRule(from_chat=False)]


@traffic_labeler.message(text='Пробка')
async def traffic(message: Message):
    city = check_user(message.from_id)[0]
    points = await get_traffic(city)
    points = int(points.replace("'", ""))
    if points == 1:
        text = f'{points} балл'
    elif 2 <= points <= 4:
        text = f'{points} балла'
    else:
        text = f'{points} баллов'

    await message.answer(f'{text} [{city}]')
