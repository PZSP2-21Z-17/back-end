from fastapi.testclient import TestClient


def test_create(client: TestClient):
    data = {
        'tag_code': 'I',
        'name': 'ijk',
    }
    response = client.post("/tag/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]


def test_all(client: TestClient):
    response = client.get("/tag/all/")
    assert response.status_code == 200
    json = response.json()
    assert len(json) == 9
    assert json[0] == {
        'tag_code': 'A',
        'name': 'abc',
    }


def test_one(client: TestClient):
    response = client.get("/tag/one/A")
    assert response.status_code == 200
    assert response.json() == {
        'tag_code': 'A',
        'name': 'abc',
    }


def test_update(client: TestClient):
    data = {
        'tag_code': 'I',
        'name': 'kji',
    }
    response = client.post("/tag/update/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_delete(client: TestClient):
    data = {
        'tag_code': 'I',
    }
    response = client.post("/tag/delete/", json=data)
    assert response.status_code == 200
