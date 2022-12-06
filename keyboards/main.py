from vkbottle import Keyboard


main_keyboard = (
    Keyboard(one_time=False, inline=False)
    .schema(
        [
            [
                {"label": "Погода", "type": "text"},
                {"label": "Пробка", "type": "text"},
            ],
            [
                {"label": "Афиша", "type": "text"},
                {"label": "Валюта", "type": "text"},
            ],
        ]
    )
    .get_json()
)
