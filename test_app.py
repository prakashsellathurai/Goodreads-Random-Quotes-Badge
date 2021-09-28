from app import app
import pytest

@pytest.fixture
def client():
    
    with app.test_client() as client:
        yield client
        
def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    
def test_get_badge(client):
    response = client.get('/getbadge?goodReadsUrl=https%3A%2F%2Fwww.goodreads.com%2Fuser%2Fshow%2F105903487-prakash-sellathurai')
    assert response.status_code == 200

def test_on_get_badge_without_url(client):
    response = client.get('/getbadge?goodReadsUrl=')
    assert response.status_code == 404

def test_on_get_badge_without_param(client):   
    response = client.get('/getbadge')
    assert response.status_code == 404
    
def test_on_get_badge_wit_iilegal_url(client):   
    response = client.get('/getbadge?goodReadsUrl=foobar')
    assert response.status_code == 404
    
def test_on_get_badge_with_contentYpe(client):
    response = client.get('/getbadge?goodReadsUrl=https%3A%2F%2Fwww.goodreads.com%2Fuser%2Fshow%2F105903487-prakash-sellathurai')
    assert response.headers["Content-Type"] == "image/svg+xml"