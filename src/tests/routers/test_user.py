from fastapi.testclient import TestClient

def test_index(client: TestClient):
    response = client.get("/user/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Log in here!"}