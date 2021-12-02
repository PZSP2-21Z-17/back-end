from fastapi.testclient import TestClient
from src.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

def test_create(client: TestClient, db: Session = Depends(get_db)):
    data = {
        'group_nr': 5,
        'exam_id': 1,
    }
    response = client.post("/group/create/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in data.keys():
        assert json[key] == data[key]
