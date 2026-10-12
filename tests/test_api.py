from fastapi.testclient import TestClient
from pygments.lexers import q
import api

client = TestClient(api.app)

def test_get_tickets_returns_empty_list(monkeypatch):
    monkeypatch.setattr(api, "get_all_tickets", lambda: [])

    response = client.get("/tickets")

    assert response.status_code == 200
    assert response.json() == []

def test_create_ticket_with_missing_fields():
    response = client.post("/tickets", json={})

    assert response.status_code == 422

def test_get_ticket_by_id_returns_404_when_not_found(monkeypatch):
    monkeypatch.setattr(api, "get_ticket_by_id", lambda ticket_id: None)

    response = client.get("/tickets/9999")

    assert response.status_code == 404

def test_get_ticket_by_id_returns_ticket(monkeypatch):
    sample_ticket = {
        "id": 1,
        "title": "Login issue",
        "description": "Unable to log in",
        "assigned_to": "Support Team",
        "status": "OPEN",
        "priority": "HIGH"
    }

    monkeypatch.setattr(
        api,
        "get_ticket_by_id",
        lambda ticket_id: sample_ticket
    )

    response = client.get("/tickets/1")

    assert response.status_code == 200
    assert response.json() == sample_ticket

def test_create_ticket_success(monkeypatch):
    def mock_create_ticket(ticket):
        ticket.id = 1
        return ticket

    monkeypatch.setattr(api, "create_ticket", mock_create_ticket)

    ticket_data = {
        "title": "Login issue",
        "description": "Unable to log in",
        "assigned_to": "Support Team",
        "priority": "HIGH"
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 201

    response_data = response.json()
    assert response_data["id"] == 1
    assert response_data["title"] == "Login issue"
    assert response_data["description"] == "Unable to log in"
    assert response_data["assigned_to"] == "Support Team"
    assert response_data["status"] == "OPEN"
    assert response_data["priority"] == "HIGH"

def test_create_ticket_with_invalid_priority():
    ticket_data = {
        "title": "Login issue",
        "description": "Unable to log in",
        "assigned_to": "Support Team",
        "priority": "SUPER_HIGH"
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 422

def test_update_ticket_success(monkeypatch):
    monkeypatch.setattr(api, "ticket_exists", lambda ticket_id: True)

    def mock_update_ticket(ticket_id, new_assigned_to, status, priority):
        return None

    monkeypatch.setattr(api, "update_ticket", mock_update_ticket)

    update_data = {
        "assigned_to": "IT Support",
        "status": "IN_PROGRESS",
        "priority": "HIGH"
    }

    response = client.put("/tickets/1", json=update_data)

    assert response.status_code == 200

def test_update_ticket_with_non_existing_ticket_id(monkeypatch):
    monkeypatch.setattr(api, "ticket_exists", lambda ticket_id: False)

    update_data = {
        "assigned_to": "IT Support",
        "status": "IN_PROGRESS",
        "priority": "HIGH"
    }

    response = client.put("/tickets/1", json=update_data)

    assert response.status_code == 404

def test_delete_ticket_success(monkeypatch):
    monkeypatch.setattr(api, "ticket_exists", lambda ticket_id: True)

    def mock_remove_ticket(ticket_id):
        return None

    monkeypatch.setattr(api, "remove_ticket", mock_remove_ticket)

    response = client.delete("/tickets/1")

    assert response.status_code == 200

def test_delete_ticket_with_non_existing_ticket_id(monkeypatch):
    monkeypatch.setattr(api, "ticket_exists", lambda ticket_id: False)

    response = client.delete("/tickets/1")

    assert response.status_code == 404

def test_get_tickets_returns_tickets(monkeypatch):
    ticket_data = {
        "id": 1,
        "title": "Login issue",
        "description": "Unable to log in",
        "assigned_to": "Support Team",
        "status": "OPEN",
        "priority": "HIGH"
    }

    monkeypatch.setattr(api, "get_all_tickets", lambda: [ticket_data])

    response = client.get("/tickets")

    assert response.status_code == 200

    response_data = response.json()
    assert response_data == [ticket_data]