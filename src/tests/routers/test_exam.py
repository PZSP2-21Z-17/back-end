from fastapi.testclient import TestClient
import datetime
from datetime import datetime
def test_create(client: TestClient):
    data = {
        'exam_id': 20,
        'date_of_exam':  str(datetime.strftime(datetime.strptime('01-01-2020', '%d-%m-%Y'),'%Y-%m-%dT%H:%M:%S')),
        'commentary': 'Destroying student lifes since 1997',
        'subject_code': 'PZSP1',
        'author_id': 1,
    }
    response = client.post("/exam/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]