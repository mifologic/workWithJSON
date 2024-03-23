import requests


"""
Что тут происходит: используется библиотека requests, чтобы выполнить get-запрос.
Ответ сохраняется в переменную response.
Циклом перебираем объекты в json из ответа.
Для каждого объекта выводится значение из поля название.

Для чего нужно: метод должен вернуть только объекты, у которых категория=women's clothing. Проверяем, что это действительно так.
Для этого проверяем категорию объектов и выводим их название. 
"""
response = requests.get('https://fakestoreapi.com/products')
print("Items in category: ")
for item in response.json():
    if item["category"] == "women's clothing":
        print(item["title"])
