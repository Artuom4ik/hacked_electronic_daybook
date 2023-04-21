# hacked_electronic_daybook
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

___
#### Это скрипт который имеет набор функций для изменения значений в базе данных. 
___
### Содержание:
* [Требования]()
* [Как пользоваться скриптом]()
* [Пример использования]()
* [Описание каждой функции]()
___
>### Для запуска программы требуется:
 * Скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * Операционная система macOS, linux, windows 7 или выше.
___
### Как пользоваться скриптом:
* Запуск Django Shell: 
    * Открываем консоль GitBash либо PowerShell.
    * Записываем в консоль команду для запуска Django Shell:
    ```python manage.py shell```
* В консоль прописываем команды для импортирования всех нужных модулей:
    ```from datacenter.models import *```
    ```from random import randint```
* В консоль записываем команду:
```schoolkid = Schoolkid.objects.get(full_name__contains="Фамилия Имя")```
* Выбираем нужную функцию.
* Копируем её в консоль.
* В консоль пишем команду для запуска функции.
___
### Описание каждой функции:
* ```fix_marks()``` - изменяет плохие отметки на хорошие.
* ```remove_chastisement()``` - удаляет замечания в электронном дневнике.
* ```create_commendation()``` - добавляет похвалу по заданному предмету за последнее пресутствие на нём.
___
### Пример работы скрипта:
#### До
![до](images/image.png)

![](images/scripts.png)

#### После
![после](images/image1.png)
