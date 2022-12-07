from vkbottle.bot import BotLabeler, rules
from vkbottle.bot import Message

from services.currency import get_currency


currency_labeler = BotLabeler()
currency_labeler.vbml_ignore_case = True
currency_labeler.auto_rules = [rules.PeerRule(from_chat=False)]


@currency_labeler.message(text='Валюта')
async def afisha(message: Message):
    data = await get_currency()
    text = 'Цена покупки в Альфа банке &#127974;\n\n'
    for item in data:
        text += f"1 {item['currency_code']} = {item['price']} &#8381;\n"
    await message.answer(text)
