from fastapi.testclient import TestClient


def test_create(client: TestClient):
    data = {
        'task_id': 2,
        'tag_code': 'B',
    }
    response = client.post("/tag_aff/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]
