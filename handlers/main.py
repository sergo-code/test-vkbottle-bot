from vkbottle.bot import BotLabeler, Message, rules
from config import bot
from keyboards import main_keyboard, choose_city_menu
from utils.sql import check_user, save_user, update_user
from vkbottle import BaseStateGroup, EMPTY_KEYBOARD

main_labeler = BotLabeler()
main_labeler.vbml_ignore_case = True
main_labeler.auto_rules = [rules.PeerRule(from_chat=False)]


class ChoiceCity(BaseStateGroup):
    city = 0


@main_labeler.message(payload={"cmd": "main"})
async def main_menu(message: Message):
    await message.answer(f"Вы вернулись в главное меню", keyboard=main_keyboard)


@main_labeler.message(text="Начать")
async def start(message: Message):
    user = await bot.api.users.get(message.from_id, fields='city')

    city = check_user(message.from_id)
    if city is not None:
        await message.answer(f"Привет! Ваш город {city[0]}", keyboard=main_keyboard)
    else:
        try:
            await message.answer(f"Привет! Ваш город {user[0].city.title}?", keyboard=choose_city_menu)
        except AttributeError:
            await bot.state_dispenser.set(message.peer_id, ChoiceCity.city)
            return "Привет! Укажи, пожалуйста, свой город"


@main_labeler.message(state=ChoiceCity.city)
async def choice_city(message: Message):
    city = message.text
    save_user(message.from_id, city)
    await bot.state_dispenser.delete(message.peer_id)
    await message.answer(f"Выбран город {city}\nЧтобы сменить город введите /city <item>", keyboard=main_keyboard)


@main_labeler.message(payload={'cmd': 'yes'})
async def choice_city(message: Message):
    user = await bot.api.users.get(message.from_id, fields='city')
    city = user[0].city.title
    save_user(message.from_id, city)
    await message.answer(f"Выбран город {city}\nЧтобы сменить город введите /city <item>", keyboard=main_keyboard)


@main_labeler.message(payload={'cmd': 'no'})
async def choice_city(message: Message):
    await bot.state_dispenser.set(message.peer_id, ChoiceCity.city)
    return 'Введите свой город'


@main_labeler.message(text=['/city <item>', '/city'])
async def choice_city(message: Message, item=None):
    if item is not None:
        update_user(message.from_id, item)
        await message.answer(f'Выбран город {item}')
    else:
        await message.answer(f'Вы не указали город')
