#from src.app import app
#from fastapi.testclient import TestClient

import requests
import json

#client = TestClient(app)

data = '''
{
  "contents": "Raise left hand",
  "score": 2,
  "date_creation": "2019-11-08T09:00:37.247426",
  "is_visible": "Y",
  "subject_code": "1",
  "author_id": 3,
  "answers": [
    {
      "content": "no",
      "is_correct": "Y",
      "task_id": 1
    },
    {
      "content": "proceed",
      "is_correct": "N",
      "task_id": 1
    }
  ]
}
'''

response = requests.post("http://127.0.0.1:8000/task/create_with_answers/", json=json.loads(data))

print(response.status_code)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=2))


