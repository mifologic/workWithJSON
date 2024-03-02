import json

"""
* Шаг 1.
  Добавляем в переменную json, с которым будем работать.
  Данные указываются в тройных кавычках, чтобы не возникало ошибки в синтаксисе 
  (например, в json true/false пишутся с маленькой буквы, а в Python - с большой)
"""
json_data = """[
  {
    "id": 1,
    "title": "Activity 1",
    "dueDate": "2024-01-09T19:03:43.1718735+00:00",
    "completed": false
  },
  {
    "id": 2,
    "title": "Activity 2",
    "dueDate": "2024-01-09T20:03:43.1718764+00:00",
    "completed": true
  },
  {
    "id": 3,
    "title": "Activity 3",
    "dueDate": "2024-01-09T21:03:43.1718768+00:00",
    "completed": false
  },
  {
    "id": 4,
    "title": "Activity 4",
    "dueDate": "2024-01-09T22:03:43.1718771+00:00",
    "completed": true
  },
  {
    "id": 5,
    "title": "Activity 5",
    "dueDate": "2024-01-09T23:03:43.1718774+00:00",
    "completed": false
  },
  {
    "id": 6,
    "title": "Activity 6",
    "dueDate": "2024-01-10T00:03:43.1718779+00:00",
    "completed": true
  },
  {
    "id": 7,
    "title": "Activity 7",
    "dueDate": "2024-01-10T01:03:43.1718782+00:00",
    "completed": false
  },
  {
    "id": 8,
    "title": "Activity 8",
    "dueDate": "2024-01-10T02:03:43.1718784+00:00",
    "completed": true
  },
  {
    "id": 9,
    "title": "Activity 9",
    "dueDate": "2024-01-10T03:03:43.1718787+00:00",
    "completed": false
  },
  {
    "id": 10,
    "title": "Activity 10",
    "dueDate": "2024-01-10T04:03:43.1718817+00:00",
    "completed": true
  },
  {
    "id": 11,
    "title": "Activity 11",
    "dueDate": "2024-01-10T05:03:43.1718821+00:00",
    "completed": false
  },
  {
    "id": 12,
    "title": "Activity 12",
    "dueDate": "2024-01-10T06:03:43.1718824+00:00",
    "completed": true
  },
  {
    "id": 13,
    "title": "Activity 13",
    "dueDate": "2024-01-10T07:03:43.1718827+00:00",
    "completed": false
  },
  {
    "id": 14,
    "title": "Activity 14",
    "dueDate": "2024-01-10T08:03:43.171883+00:00",
    "completed": true
  },
  {
    "id": 15,
    "title": "Activity 15",
    "dueDate": "2024-01-10T09:03:43.1718833+00:00",
    "completed": false
  },
  {
    "id": 16,
    "title": "Activity 16",
    "dueDate": "2024-01-10T10:03:43.1718837+00:00",
    "completed": true
  },
  {
    "id": 17,
    "title": "Activity 17",
    "dueDate": "2024-01-10T11:03:43.171884+00:00",
    "completed": false
  },
  {
    "id": 18,
    "title": "Activity 18",
    "dueDate": "2024-01-10T12:03:43.1718844+00:00",
    "completed": true
  },
  {
    "id": 19,
    "title": "Activity 19",
    "dueDate": "2024-01-10T13:03:43.1718848+00:00",
    "completed": false
  },
  {
    "id": 20,
    "title": "Activity 20",
    "dueDate": "2024-01-10T14:03:43.1718851+00:00",
    "completed": true
  },
  {
    "id": 21,
    "title": "Activity 21",
    "dueDate": "2024-01-10T15:03:43.1718854+00:00",
    "completed": false
  },
  {
    "id": 22,
    "title": "Activity 22",
    "dueDate": "2024-01-10T16:03:43.1718858+00:00",
    "completed": true
  },
  {
    "id": 23,
    "title": "Activity 23",
    "dueDate": "2024-01-10T17:03:43.1718861+00:00",
    "completed": false
  },
  {
    "id": 24,
    "title": "Activity 24",
    "dueDate": "2024-01-10T18:03:43.1718864+00:00",
    "completed": true
  },
  {
    "id": 25,
    "title": "Activity 25",
    "dueDate": "2024-01-10T19:03:43.1718867+00:00",
    "completed": false
  },
  {
    "id": 26,
    "title": "Activity 26",
    "dueDate": "2024-01-10T20:03:43.171887+00:00",
    "completed": true
  },
  {
    "id": 27,
    "title": "Activity 27",
    "dueDate": "2024-01-10T21:03:43.1718874+00:00",
    "completed": false
  },
  {
    "id": 28,
    "title": "Activity 28",
    "dueDate": "2024-01-10T22:03:43.1718877+00:00",
    "completed": true
  },
  {
    "id": 29,
    "title": "Activity 29",
    "dueDate": "2024-01-10T23:03:43.171888+00:00",
    "completed": false
  },
  {
    "id": 30,
    "title": "Activity 30",
    "dueDate": "2024-01-11T00:03:43.1718883+00:00",
    "completed": true
  }
]
"""

"""
* Шаг 2.
  Преобразуем json в python-объект. Для этого используется встроенная библиотека json.
  Можно проверить, какой тип данных у нас в итоге получился, чтобы понимать, как с ним дальше работать
"""
data_from_json = json.loads(json_data)
print(type(data_from_json))  # выводим тип данных, необязательный шаг

"""
* Шаг 3.
  Получаем нужные данные: цикл проходится по всему массиву данных (в данном случае – списку),
  берёт каждый объект и для него выводит значение из поля title.
"""
for item in data_from_json:
    print(f"Item title={item['title']}")
