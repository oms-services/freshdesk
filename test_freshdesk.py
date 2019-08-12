from http import HTTPStatus
import os
import warnings

def test_createTicket_request(client):
    global id
    data = {
        "description": "Details about the issue...",
        "subject": "Support Needed...",
        "email": "tom@outerspace.com",
        "cc_emails": [
            "ram@freshdesk.com",
            "diana@freshdesk.com"
        ]
    }
    url = "/ticket/create"
    response = client.post(url, json=data)
    id = response.json.get("id")
    assert response.status_code == HTTPStatus.CREATED

def test_getTicket_request(client):
    global id
    data = {
        "id":id
    }
    url = "/ticket/get"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_deleteTicket_request(client):
    global id
    data = {
        "id":id
    }
    url = "/ticket/delete"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_deleteTicket_request_fail(client):
    global id
    data = {
        "id":id
    }
    url = "/ticket/delete"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_listTicket_request(client):
    url = "/ticket/list"
    response = client.post(url)
    assert response.status_code == HTTPStatus.OK

def test_createContact_request(client):
    global id
    data = { 
        "name":"Mock name", 
        "email":"test.mock111@freshdesk.com"
    } 
    url = "/contact/create"
    response = client.post(url, json=data)
    id = response.json.get("id")
    assert response.status_code == HTTPStatus.CREATED

def test_getContact_request(client):
    global id
    data = {
        "id":id
    }
    url = "/contact/get"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_deleteContact_request(client):
    global id
    data = {
        "id":id
    }
    url = "/contact/delete"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_deleteContact_request_fail(client):
    global id
    data = {
        "id":id
    }
    url = "/contact/delete"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_listContact_request(client):
    url = "/contact/list"
    response = client.post(url)
    assert response.status_code == HTTPStatus.OK