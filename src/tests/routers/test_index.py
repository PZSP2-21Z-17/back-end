from fastapi.testclient import TestClient
from src.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

def test_index(client: TestClient, db: Session = Depends(get_db)):
    response = client.get("/")
    assert response.status_code == 200