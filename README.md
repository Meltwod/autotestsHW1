# Проект AutotestsHW1
### Это проект, созданный для практики домашних заданий с курсов до Авто-тестированию на языке Python.

#### Все тесты разработаны и запускаются в программе PyCharm CE, на ОС Linux/Ubuntu.

#
## Подготовка к запуску проекта:
#### 1) Устанавливаем PyCharm CE [ *sudo snap install pycharm-community --classic* ]
#### 2) Создание виртуального коружения Python 3.10.4. [ *python -m venv env* ]
#### 3) Запустить виртуальное окружение [ *source env/bin/activate* ]
#### 4) Обновить pip [ *pip install -U pip* ] 
#### 5) Установить pytest через зависимость (pytest 7.1.2)
#### 6) Установить request [ *pip install requests* ]

#
## Запуск 1_test_one:
#### Для запуска тестов используем [ *pytest 1_test_one -s -v* ]

### Описание 1_test_one:
#### Файл содержит 28 тестов. Некоторые тесты содержат параметризацию, многие обращаются к фикстурам с файла conftest.py из корня проекта.
#### 1 тест проходит рандомно, т.к. реализован с помощью генерации случайного числа, с последующей проверкой на совпадение.
#### Используются фикстуры с запуском в начале и конце сессии и модуля. 

# 

## Запуск 2_test_API:
#### Для запуска тестов используем [ *pytest 2_test_API --put=\*Порода собаки\* --amount=\*Количество слуйчайных фото одним запросом\* -s -v* ]

### Описание 2_test_API:
#### Используется API https://dog.ceo/dog-api/documentation
#### Файл содержит 31 тест. Некоторые тесты содержат параметризацию, многие обращаются к фикстурам с файла conftest.py из папки теста.
#### В параметр --put кладём любую породу собаки из API (https://dog.ceo/dog-api/breeds-list).
#### В параметр --amount кладём число, которое отправит нужное количество случайных фото. (https://dog.ceo/dog-api/documentation/random)
#### Все тесты проходят. На выходе должны получить у всех запросов код 200, рабочие ссылки с запросов. Также нужное количество рандомных фото указаных в параметре --amount.


