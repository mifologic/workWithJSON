# Работа с JSON на Python

В проекте показаны три варианта работы с json в Python:
* сохранение в переменную (папка json_as_variable);
* чтение из файла (папка json_from_file);
* вызов метода API (папка json_from_request).

### Используемые библиотеки
* json;
* [requests](https://requests.readthedocs.io/en/latest/).

## Запуск проекта локально
Запустить терминал, в нём ввести команду:
```commandline
git clone https://github.com/mifologic/workWithJSON.git
```

### Запуск из командной строки
Файлы можно запустить из терминала. Для запуска папки json_from_request потребуется установить библиотеку requests. 
Команда для установки:
````commandline
python -m pip install requests
````
**NB!** В некоторых операционных системах python может запускаться командой, например, python3. 

Чтобы запустить файлы из папки, нужно в терминале перейти в эту папку. После этого ввести команду:
```commandline
python file_name.py
```
Вместо file_name указать имя нужного файла.

Или для запуска всех файлов ввести команду (unix-system):
```commandline
ls *.py|xargs -n 1 -P 4 python
```

