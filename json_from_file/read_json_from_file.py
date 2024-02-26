import json

# открываем файл и сохраняем данные из него в переменную json_form_file
with open('data.json') as file:
    json_form_file = json.load(file)


# перебираем данные в цикле и выводим каждый из объектов
for item in json_form_file:
    print(item)
