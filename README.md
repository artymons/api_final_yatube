Yatube api
api соц сеть

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram
Cоздать и активировать виртуальное окружение:

python -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver

Использование
Расскажите как установить и использовать ваш проект, покажите пример кода:

Установите npm-пакет с помощью команды:

$ npm i your-awesome-plugin-name
Получение публикаций
Получить список всех публикаций.