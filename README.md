# Веб-приложение опросов Django
Данный проект позволяет создавать опросы и проходить их с выбором разных вариаций опросов.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Команда проекта](#команда-проекта)

## Технологии
- [Django](https://www.djangoproject.com/)
- [DRF](https://www.django-rest-framework.org/)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html)

## Начало работы

Сперва нужно установить все необходимые зависимости
```commandline
pip install -r requirements.txt
```

Перейти в основную папку проекта, где находится файл manage.py
```commandline
cd /polls/
```

Выполнить все миграции 
```commandline
python manage.py makemigrations
python manage.py migrate
```

Если все миграции выполнились без ошибок, веб-приложение будет доступно по адресу 127.0.0.1:8000 после команды
```commandline
python manage.py runserver
```

## Команда проекта
Проект разрабатывался:
- Хрипунов Иван - backend-азработчик 