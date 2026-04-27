# 🤖 Telegram & VK боты с Dialogflow
## 🧠 Что это за боты?
Это два корпоративных чат-бота (для Telegram и ВКонтакте), которые используют Dialogflow (NLU-платформа от Google) для понимания естественного языка. Боты отвечают на вопросы пользователей/
Оба бота подключены к одному агенту Dialogflow, поэтому все сценарии ответов управляются централизованно.
## 🎥 Пример работы
![tg_bot](https://raw.githubusercontent.com/Andrey9045/gif/refs/heads/main/TG_bot.gif)
![vk_bot](https://raw.githubusercontent.com/Andrey9045/gif/refs/heads/main/Vk_bot.gif)


## ✨ Что такое Dialogflow и зачем он нужен?
Dialogflow ES — это облачный сервис от Google для распознавания намерений и сущностей. Он позволяет:

Создавать «интенты» (например, Устройство на работу, Забыл пароль, Удалить аккаунт).

Обучать их десятками фраз-примеров.

Получать ответы на русском языке без написания сложных регулярок.

Благодаря Dialogflow боты:

Понимают синонимы («как устроиться», «хочу работать», «возможно ли трудоустройство»).

Не требуют перезапуска после изменения сценариев (всё редактируется в веб-консоли).

Могут подключаться к любым мессенджерам через один API.

## 🚀 Запущенные версии ботов
TG_BOT - [@gameverbsbot](@gameverbsbot)
VK_BOT - [club238077424](club238077424)


## ⚙️ Как это работает (архитектура)
Пользователь пишет сообщение в Telegram или VK.

Сервер получает событие через Long Poll (для VK) или polling (для Telegram).

Текст отправляется в Dialogflow через detectIntent.

Dialogflow возвращает распознанный интент и ответную фразу.

Бот отправляет ответ пользователю.

Все секреты (токены, ключи) хранятся в файле .env

## Локальный запуск (для разработки)
### Установка бота
`git clone https://github.com/Andrey9045/game_verbs_bot.git`
`cd game_verbs_bot`
### Установка виртуального окуружения
```
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
### Создайте файл .env с вашими токенами
```
TG_TOKEN=1234567890:AAElE... (токен Telegram бота)
VK_TOKEN=vk1.a... (токен VK сообщества)
GOOGLE_APPLICATION_CREDENTIALS=/opt/game_verbs_bot/credentials.json
```
* `GOOGLE_APPLICATION_CREDENTIALS` - Сюда нужно положить абсолютный путь до credentials.json(Можно получить в Google Cloud Console)

### Обучие dialogflow
Вы можете обучить dialogflow с помощью скрипта intent_create.py
- Создайте файл questions.json формата:
```
{
  "Устройство на работу": {
    "questions": ["Как устроиться?", "Хочу работать"],
    "answer": "Напишите на почту game-of-verbs@gmail.com"
  }
}
```
Положите этот файл в корень проекта.
- Запустите скрипт
```
python intent_create.py
```

### Запуск ботов
Локально моожно запустить в двух паралельно запущенных терменалов
```
python bot.py
```
```
python bot_vk.py
```

### Контактные данные
Gmail: andreidikun123@gmail.com
TG: @dikunand

