from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Book
from users.models import CustomUser

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return CustomUser.objects.create_user(
        email='test@example.com',
        password='testpassword'
    )

@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def book(user):
    return Book.objects.create(
        user=user,
        name='Test Book',
        author='Test Author',
        pages_amount=200,
        description='Test description',
        reading_status='will_read'
    )

@pytest.mark.django_db
class TestBookAPI:
    
    def test_book_list(self, authenticated_client, book):
        url = reverse('book_list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['name'] == 'Test Book'
    
    def test_book_create(self, authenticated_client):
        url = reverse('book_create')
        data = {
            'name': 'New Book',
            'author': 'New Author',
            'pages_amount': 300,
            'description': 'New description',
            'reading_status': 'will_read'
        }
        response = authenticated_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 1
        assert Book.objects.first().name == 'New Book'
    
    def test_book_details(self, authenticated_client, book):
        url = reverse('book_details', kwargs={'book_id': book.id})
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Test Book'
    
    def test_book_delete(self, authenticated_client, book):
        url = reverse('book_delete', kwargs={'book_id': book.id})
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Book.objects.count() == 0
