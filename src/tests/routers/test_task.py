from fastapi.testclient import TestClient
from datetime import datetime


def test_task_create(client: TestClient):
    data = {
        'task_id': 19,
        'contents': 'If yes say no?',
        'score': 20,
        'date_creation': str(datetime.strftime(datetime.strptime('01-01-2020', '%d-%m-%Y'), '%Y-%m-%dT%H:%M:%S')),
        'is_visible': 'F',
        'subject_code': 'PZSP1',
        'author_id': 1,
    }
    response = client.post("/task/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]


def test_update(client: TestClient):
    data = {
        'task_id': 7,
        'contents': 'If yes say no, or commit to github your newest changes?',
        'score': 20,
        'date_creation': str(datetime.strftime(datetime.strptime('02-01-2020', '%d-%m-%Y'), '%Y-%m-%dT%H:%M:%S')),
        'is_visible': 'F',
        'subject_code': 'PZSP1',
        'author_id': 1,
    }
    response = client.post("/task/update/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_delete(client: TestClient):
    data = {
        'task_id': 5,
    }
    response = client.post("/task/delete/", json=data)
    assert response.status_code == 200
