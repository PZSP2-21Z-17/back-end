from fastapi.testclient import TestClient
import datetime
from datetime import datetime
def test_task_create(client: TestClient):
    data = {
        'task_id': 20,
        'contents': 'If yes say no?',
        'score': 20,
        'date_creation':  str(datetime.strftime(datetime.strptime('01-01-2020', '%d-%m-%Y'),'%Y-%m-%dT%H:%M:%S')),
        'is_visible': 'F',
        'subject_code': 'PZSP1',
        'author_id': 1,
    }
    response = client.post("/task/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]