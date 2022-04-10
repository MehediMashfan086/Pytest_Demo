from urllib import response
import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        first_name= "Mehedi",
        last_name = "Hasan",
        email = "mehedi@gmail.com",
        password = "Pass@123"
    )
    
    response = client.post('/api/register/', payload)
    
    data = response.data
    
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert "password" not in data
    assert data["email"] == payload["email"]
    
    
@pytest.mark.django_db
def test_login_user(user, client):
    
    response = client.post("/api/login/", dict(email = "mh@gmail.com", 
                                               password = "mh@123"))
    
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post("/api/login/", dict(email = "mhd@gmail.com", 
                                               password = "12345"))
    
    assert response.status_code == 403
    
@pytest.mark.django_db
def test_get_me(user, auth_client):

    response = auth_client.get("/api/me/")
    
    assert response.status_code == 200
    
    data = response.data
    assert data["id"] == user.id
    assert data["email"] == user.email
    
@pytest.mark.django_db
def test_logout(auth_client):
    response = auth_client.post("/api/logout/")
    
    assert response.status_code == 200
    assert response.data["message"] == "so long farewell"