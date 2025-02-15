from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views


class TestUrls(SimpleTestCase):
     def test_register_user(self):
        url = reverse('users:register_user')
        self.assertEqual(resolve(url).func, views.register_user)
    
     def test_register_employee(self):
        url = reverse('users:register_employee')
        self.assertEqual(resolve(url).func, views.register_employee)

     def test_login(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func, views.login_view)
    
     def test_logout(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, views.logout_view)
    
     def test_register(self):
        url = reverse('users:register')
        self.assertEqual(resolve(url).func, views.register)
    
     def test_register_third_person(self):
        url = reverse('users:register_third_person')
        self.assertEqual(resolve(url).func, views.register_third_person)
    
     def test_add_employee(self):
        url = reverse('users:add_employee')
        self.assertEqual(resolve(url).func, views.add_employee)