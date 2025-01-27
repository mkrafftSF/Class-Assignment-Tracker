import pytest

def test_create_assignment(client, access_token):
    response = client.post(
        '/api/assignments',
        json={
            "title": "New Assignment",
            "description": "Assignment description",
            "due_date": "2025-12-31T23:59:59"
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 201
    assert response.json['title'] == "New Assignment"

def test_get_assignments(client, access_token):
    response = client.get(
        '/api/assignments',
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json, list)
