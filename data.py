import random


BASE_URL = "https://qa-desk.stand.praktikum-services.ru"
USER_PASSWORD = "StrongPassword123"
NAME_PRODUCT = "Горе от ума"
PRICE_PRODUCT = 598
ABOUT_PRODUCT = "Комедия в стихах русского поэта и драматурга Александра Сергеевича Грибоедова, его наиболее известное произведение"
CITY = random.choice(
    [
        "Москва",
        "Санкт-Петербург",
        "Новосибирск",
        "Екатеринбург",
        "Нижний Новгород",
        "Казань",
    ]
)
CATEGORY = "Книги"
