# Работа с JSON на Python

В проекте показаны три варианта работы с json в Python:
* сохранение в переменную (папка json_as_variable);
* чтение из файла (папка json_from_file);
* вызов метода API (папка json_from_request).

### Используемые библиотеки
* json (входит в стандартные библиотеки Python, не требует дополнительной установки);
* [requests](https://requests.readthedocs.io/en/latest/).

## Запуск проекта локально
На компьютере должен быть установлен Python. Инструкция по установке: 
[Windows](https://metanit.com/python/tutorial/1.2.php),
[MacOS](https://metanit.com/python/tutorial/1.5.php),
[Linux](https://metanit.com/python/tutorial/1.6.php).

Запустить терминал. Ввести команду, чтобы скопировать проект к себе на компьютер (будет скопирован в текущую папку):
```commandline
git clone https://github.com/mifologic/workWithJSON.git
```

### Запуск из командной строки
Файлы можно запустить из терминала. Для запуска папки json_from_request потребуется установить библиотеку requests. 
Команда для установки:
````commandline
python -m pip install requests
````
**NB!** В некоторых операционных системах python может запускаться другой командой, например, python3. 

Чтобы запустить файлы из папки, нужно в терминале перейти в эту папку. После этого ввести команду:
```commandline
python file_name.py
```
Вместо file_name указать имя нужного файла.

Или для запуска всех файлов ввести команду (macOS, Linux):
```commandline
ls *.py|xargs -n 1 -P 4 python
```

### Другие варианты запуска
Также код можно открыть в удобной вам среде разработки, поддерживающей Python. 
Для запуска может потребоваться виртуальное окружение. Подробнее о нём можно почитать [здесь](https://pavel-karateev.gitbook.io/intermediate-python/sredstva-razrabotki/virtual_environment). 
