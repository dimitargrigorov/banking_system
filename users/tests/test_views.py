from django.urls import reverse
from django.test import TestCase, Client
from users.models import CustomUser,Employee,CreateEmployee
from users.forms import CustomUserCreationForm


class TestRegiterUser(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_user_valid_form(self):
        response = self.client.post(reverse('users:register_user'),{
            'username':'testuser',
            'email':'testuser@gmail.com',
            'egn':'4124123',
            'age':24,
            'password1':'Testtest2025!',
            'password2':'Testtest2025!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('posts:welcome'))

    def test_register_user_role_equal_to_user(self):
        response = self.client.post(reverse('users:register_user'),{
            'username':'testuser',
            'email':'testuser@gmail.com',
            'egn':'4124123',
            'age':24,
            'password1':'Testtest2025!',
            'password2':'Testtest2025!'
        })
        self.assertEqual(CustomUser.objects.get(username='testuser').role, 'Клиент')

    def test_register_user_not_metod_POST(self):
        response = self.client.get(reverse('users:register_user'))
        self.assertTemplateUsed(response, 'register_user.html')


