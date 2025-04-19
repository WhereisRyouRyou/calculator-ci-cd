import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/calc?a=5&b=3&op=add')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 8

def test_subtract(client):
    response = client.get('/calc?a=10&b=3&op=sub')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 7

def test_multiply(client):
    response = client.get('/calc?a=2&b=3&op=mul')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 6

def test_divide(client):
    response = client.get('/calc?a=10&b=2&op=div')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 5

def test_divide_by_zero(client):
    response = client.get('/calc?a=10&b=0&op=div')
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == 'Division by zero is not allowed'

def test_invalid_operation(client):
    response = client.get('/calc?a=10&b=2&op=xyz')
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == 'Invalid operation'

def test_invalid_input(client):
    response = client.get('/calc?a=abc&b=3&op=add')
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == 'Invalid input'
