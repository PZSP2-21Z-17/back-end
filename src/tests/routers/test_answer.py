from fastapi.testclient import TestClient

def test_create(client: TestClient):
    data = {
        'answer_id': 73,
        'content': 'Bababui',
        'is_correct': 't',
        'task_id': 1,
    }
    response = client.post("/answer/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]
