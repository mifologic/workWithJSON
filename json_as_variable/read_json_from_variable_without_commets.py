import json

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
  }
]
"""

for item in json.loads(json_data):
    print("Is activity completed?")
    print(item['completed'])
