# Sarafan_market

## 1 задание - в файле the_first_task.py

## Grocery_Store
Сервис позволяет:
- создавать категории
- создавать подкатегории
- создавать товары
- присваивать товарам категории
- добавлять и удалять товары в корзине
- очищать корзину целиком

## Стек технологий
- Python 3.11
- Django 3.2
- djangorestframework 3.13

## Запуск проекта
- Сделать форк репозитория https://github.com/Glebchik57/Sarafan_market
- Склонировать репозиторий на свой компьютер
```
git clone ...
```
- Cоздать и активировать виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции

```
python manage.py makemigrations
python manage.py migrate
```


- Запустить проект

```
python manage.py runserver
```

## Автор
[Sevostyanov Gleb](https://github.com/Glebchik57)