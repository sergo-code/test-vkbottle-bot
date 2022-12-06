from pyowm import OWM


def get_weather(city):
    owm = OWM('b1da258166c05ed4bf6b60d992e8d342')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temperature = weather.temperature("celsius")
    return temperature
