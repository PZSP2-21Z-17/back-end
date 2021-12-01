from fastapi.testclient import TestClient
from src.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

def test_login(client: TestClient, db: Session = Depends(get_db)):
    data = {
        'e_mail': 'bartek@gmail.com',
        'password': 'Bartek',
    }
    response = client.post("/user/login/", json=data)
    assert response.status_code == 200

def test_register(client: TestClient, db: Session = Depends(get_db)):
    data = {
        'e_mail': 'unique@email.com',
        'password': 'balbinka',
        'first_name': 'chedar',
        'last_name': 'cheese',
    }
    response = client.post("/user/register/", json=data)
    assert response.status_code == 200
    json = response.json()
    for key in ['e_mail', 'first_name', 'last_name']:
        assert json[key] == data[key]
    assert json.get('user_id') is not None

def test_lookup(client: TestClient, db: Session = Depends(get_db)):
    response = client.get("/user/lookup/1")
    assert response.status_code == 200