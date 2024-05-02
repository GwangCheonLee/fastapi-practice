from fastapi.testclient import TestClient
from httpx import Response

from main import app

client: TestClient = TestClient(app)


def test_read_main():
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ''
