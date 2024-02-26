import requests


# выводим все объекты из json в ответе
response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=pending')
for item in response.json():
    print(item)

print("\n")


"""
Что тут происходит: используется библиотека requests, чтобы выполнить get-запрос.
Ответ сохраняется в переменную response.
Циклом перебираем объекты в json из ответе.
Для каждого объекта выводим значение из поля статус.

Для чего нужно: метод должен вернуть только объекты, у которых статус=pending. Проверяем, что это действительно так.
"""
# response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=pending')
# for item in response.json():
#     print(item['status'])
