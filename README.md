# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Сияние". Если Вы попали в этот репозиторий случайно, то Вы не сможете его запустить т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД. 

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников.

## Как установить

Переменные окружения

DB_PORT - Порт БД

DB_HOST - Хост БД

DB_USER - Пользователь

DB_PASSWORD - Пароль

DB_NAME - Имя базы

DB_ENGINE - Движок БД

DB_SECRET_KEY - Секретный ключ БД

Они необходимы для доступа в базу данных.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
Далее запустить сервер в командной строке:

```
python manage.py runserver 0.0.0.0:8000.
```

## Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
