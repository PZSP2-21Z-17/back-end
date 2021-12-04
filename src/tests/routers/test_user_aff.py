from fastapi.testclient import TestClient

def test_create(client: TestClient):
    data = {
        'subject_code': 'PZSP3',
        'user_id': 1,
    }
    response = client.post("/user_aff/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]