import json
from unittest.mock import patch
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .views import EmployeeLogin, EmployeeLogout, EmployeePasswordReset

class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse("employee_login")
        self.logout_url = reverse("employee_logout")
        self.password_reset_url = reverse("employee_password_reset")
        self.user= get_user_model().objects.create_user(username="test", email="test@test.com", password="testpassword")

    def tearDown(self) -> None:
        self.user.delete()
    # Check if csrftoken is being returned
    def test_login_get_csrf_token(self):
        response = self.client.get(reverse('employee_login'))
        self.assertContains(response, 'X-CSRFToken')
    # Create a user and check if login is successful
    @patch('jwt.encode')
    def test_login_success(self, mock_encode):
        mock_encode.return_value = "fake_token"
        data = {"username": "test", "password": "testpassword",}
        response = self.client.post(path=self.login_url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"access_token": "fake_token"})
        self.assertEqual(mock_encode.call_count, 1)

    def test_logout_get_csrf_token(self):
        response = self.client.get(reverse('employee_logout'))
        self.assertContains(response, 'X-CSRFToken')
        
    def test_logout_success(self):
        self.client.login(username='test', password='testpassword')
        response = self.client.post(reverse('employee_logout'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'success': 'True'})


    def test_pwr_get_csrf_token(self):
        response = self.client.get(reverse('employee_password_reset'))
        self.assertContains(response, 'X-CSRFToken')

    @patch('apps.management.models.Employee.set_password')  
    @patch('apps.management.models.Employee.save')
    def test_password_reset_success(self, mock_save, mock_set_password):
        user = get_user_model().objects.create_user('test', 'test@test.com', 'oldpassword')
        data = {'username': 'test', 'password': 'newpassword'}
        response = self.client.post(reverse('employee_password_reset'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'success': 'True'})
        mock_set_password.assert_called_with('newpassword')
        mock_save.assert_called()