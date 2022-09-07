# yamdb_final

![yamdb workflow](https://github.com/KzarSnake/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


api_yamdb - Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 

## Стек: 
* Python 3
* Django 2.2 LTS
* Django REST Framework
* SQLite3
* Simple-JWT
* GIT

## Установка:

Создать и заполнить файл .env по образцу 

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Собрать и запустить контейнер с помощью команды

`docker-compose up -d --build`

Выполнить миграции с помощью команды

`docker-compose exec web python manage.py migrate`

Собрать статику с помощью команды

`docker-compose exec web python manage.py collectstatic --no-input`

Создать суперпользователя с помощью команды

`docker-compose exec web python manage.py createsuperuser`

Заполнить базу с помощью команды

`docker-compose exec web python manage.py loaddata fixtures.json`

## Автор:
[Свашенко Денис](https://github.com/KzarSnake)