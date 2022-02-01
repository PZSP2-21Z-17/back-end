from fastapi.testclient import TestClient


def test_create(client: TestClient):
    data = {
        'group_nr': 1,
        'exam_id': 1,
        'task_id': 18,
        'nr_on_sheet': 7,
    }
    response = client.post("/task_aff/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]
