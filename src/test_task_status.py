import pytest
from custom_prom import task_status

@pytest.fixture
def client():
    task_status.config['TESTING'] = True
    with task_status.test_client() as client:
        yield client

def test_receive_task_success(client):
    response = client.post('/api/tasks', json={
        "tool": "upgrader",
        "task": "healthchecks",
        "status": "completed",
        "duration": 120
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Task received"}

def test_receive_task_invalid_data(client):
    response = client.post('/api/tasks', json={
        "tool": "upgrader",
        "task": "healthchecks",
        "duration": 120
    })
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid task data"}