# Проект Yatube(api)

## Описание

Api для портала блогеров Yatube 


## Установка

1. Клонировать репозиторий

2. Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```

3. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python3 manage.py migrate
```

5. Запустить проект:
```
python3 manage.py runserver
```

## Примеры запросов

Получить список всех постов
/api/v1/posts/

Получить пост по id
/api/v1/posts/{id}/
