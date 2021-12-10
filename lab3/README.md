# Lab3

### 1) Створив папку з назвою лабораторної роботи у власному репозиторії. Виконав наступні команди:
#### pipenv --python 3.7
#### pipenv install django
### 2) За допомогою Django Framework створив заготовку проекту. Виконав наступні команди: 
#### pipenv run django-admin startproject my_site

#### mv my_site/my_site/* my_site/
#### mv my_site/manage.py ./
### 3) Все встановилось правильно і я запустив сервер. Виконав команду:
#### pipenv run python manage.py runserver
#### Все запустилось успішно
### 4)Створив шаблон додатку за допомогою команди
#### pipenv run python manage.py startapp main
### 5) Створив main.html та urls.py
### 6) Заповнив потрібні файли, а також перевірив правильність виконання, модифікувала функцію  health.
### 7) Створив файл monitoring.py, який за допомогою бібліотеки requests буде опитувати сторінку health. Встановив дану бібліотеку за допомогою команди: 
#### pipenv install requests
### 8) Спростив роботу з середовищем. Закомітив файл логів server.log 
