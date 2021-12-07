# FAQ-бот для волонтёров

## Возможности
На момент написания бот может приветсвовать пользователя, а так же пытаться угадывать то, что ему нужно с помощью *TF-IDF* анализа вопроса пользователя.

## Установка

### 1. Зависимости
Для корректной работы бота необходимы следующие библиотеки Python:

- `python-telegram-bot`
- `numpy`
- `pymorphy2`
- `stopwords`

Их можно установить командой `pip install python-telegram-bot numpy pymorphy2 stopwords`

### 2. Токен
Для любого Telegram-бота необходим токен доступа, который (как и сам аккаунт бота) можно получить у [BotFather](https://t.me/botfather).

После того, как у вас имеется токен, вам необходимо клонировать репозиторий и перейти в файл `bot.py`. На 6 строчке нужно заменить `"epic_token"` на ваш токен, обёрнутый в двойные кавычки.


### 3. Запуск
После смены токена на ваш собственный, бота можно запустить командой `python bot.py`.

