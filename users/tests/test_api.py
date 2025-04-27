import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import CustomUser


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
        "password2": "testpassword123",
    }


@pytest.fixture
def created_user():
    return CustomUser.objects.create_user(
        username="existinguser",
        email="existing@example.com",
        password="existingpassword",
    )


@pytest.mark.django_db
class TestUserAPI:
    def test_user_registration(self, api_client, user_data):
        url = reverse("register")
        response = api_client.post(url, user_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert "access_token" in response.data
        assert "refresh_token" in response.data
        assert CustomUser.objects.count() == 1
        assert CustomUser.objects.get().email == "test@example.com"

    def test_user_login(self, api_client, created_user):
        url = reverse("login")
        data = {
            "email": "existing@example.com",
            "password": "existingpassword",
        }
        response = api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert "access_token" in response.data
        assert "refresh_token" in response.data

    def test_user_profile(self, api_client, created_user):
        api_client.force_authenticate(user=created_user)
        url = reverse("profile")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == "existinguser"

    def test_user_profile_update(self, api_client, created_user):
        api_client.force_authenticate(user=created_user)
        url = reverse("update_profile")
        data = {"username": "updateduser"}
        response = api_client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        created_user.refresh_from_db()
        assert created_user.username == "updateduser"
