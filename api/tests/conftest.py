import pytest
from rest_framework.test import APIClient
from user import services as user_services

@pytest.fixture
def user():
    user_dc = user_services.UserDataClass(
        first_name="Mehedi",
        last_name="Hasan",
        email="mh@gmail.com",
        password="mh@123"
    )
    
    user = user_services.create_user(user_dc=user_dc)
    return user


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def auth_client(user, client):
    client.post("/api/login/", dict(email = user.email, password="mh@123"))
    
    return client