from config import labeler, bot
from handlers import main_labeler, weather_labeler, afisha_labeler, currency_labeler, traffic_labeler


labeler.load(main_labeler)
labeler.load(weather_labeler)
labeler.load(afisha_labeler)
labeler.load(currency_labeler)
labeler.load(traffic_labeler)

bot.labeler = labeler

bot.run_forever()
