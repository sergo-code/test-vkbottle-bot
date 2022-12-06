from config import labeler, bot
from handlers import main_labeler, weather_labeler, afisha_labeler


labeler.load(main_labeler)
labeler.load(weather_labeler)
labeler.load(afisha_labeler)

bot.labeler = labeler

bot.run_forever()
