import json

"""
* Шаг 1.
  Открываем файл и сохраняем данные из него в переменную json_form_file.
  Для работы с файлом использована встроенная библиотека json.
"""
with open('data.json') as file:
    json_form_file = json.load(file)


"""
* Шаг 2.
  Перебираем данные в цикле и выводим каждый из объектов.
"""
for item in json_form_file:
    print(item)
