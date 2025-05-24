import pytest
from model import app
import requests
import requests_mock

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_status_success(client):
    org_name = ""
    model_name = ""
    endpoint_name = f"{org_name}/{model_name}"
    url = "https://api.endpoints.huggingface.cloud/v1/endpoints"
    endpoint_url = f"{url}/{endpoint_name}"

    with requests_mock.Mocker() as m:
        m.get(endpoint_url, json={"status": "RUNNING"}, status_code=200)

        response = client.get("/status", json={"model_name": model_name})
        data = response.get_json()

        assert response.status_code == 200
        assert data["status"] == "RUNNING"