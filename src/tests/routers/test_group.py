from fastapi.testclient import TestClient

def test_create(client: TestClient):
    data = {
        'group_nr': 5,
        'exam_id': 1,
    }
    response = client.post("/group/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]
