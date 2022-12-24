# api_yatube

## Описание
Учебный проект Яндекс.Практикума.
Api социальной сети, которая позволяет создавать посты, присваивать группу, комментировать записи, подписываться на пользователей

## Технологии
Python 3.7.9 Django 3.2.16

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
> git clone git@github.com:UmLilia/api_final_yatube.git
> cd api_final_yatube
Cоздать и активировать виртуальное окружение:
> python -m venv env
> source venv/Scripts/activate
Установить зависимости из файла requirements.txt:
> python -m pip install --upgrade pip
> pip install -r requirements.txt
Выполнить миграции:
> python manage.py migrate
Запустить проект:
> python manage.py runserver

## Автор:
Лилия Уманец