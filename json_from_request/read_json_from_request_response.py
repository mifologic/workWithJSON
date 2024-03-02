import requests


"""
Что тут происходит: используется библиотека requests, чтобы выполнить get-запрос.
Ответ сохраняется в переменную response.
Циклом перебираем объекты в json из ответа.
Для каждого объекта выводится значение из поля статус.

Для чего нужно: метод должен вернуть только объекты, у которых статус=pending. Проверяем, что это действительно так.
Для этого выводим статус объектов. Также добавлена проверка через assert.
"""
response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=pending')
for item in response.json():
    print(f"Item status={item['status']}")
    assert item['status'] == 'pending'
