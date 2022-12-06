import os
from dotenv import load_dotenv

from vkbottle import Bot, CtxStorage, API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler


load_dotenv()

api = API(os.getenv('TOKEN'))
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
bot = Bot(api=api, state_dispenser=state_dispenser)
ctx = CtxStorage()
