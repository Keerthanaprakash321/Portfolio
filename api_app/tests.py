from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from projects_app.models import Project

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            tech_stack="Python, Django",
            slug="test-project"
        )

    def test_project_list(self):
        url = reverse('api_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_project_detail(self):
        url = reverse('api_project_detail', kwargs={'slug': 'test-project'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Project")

    def test_contact_create_api(self):
        url = reverse('api_contact_create')
        data = {
            'name': 'API User',
            'email': 'api@example.com',
            'subject': 'API Subject',
            'message': 'API Message'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


