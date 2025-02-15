from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts import views


class TestUrls(SimpleTestCase):

    def test_profile(self):
        url = reverse('posts:profile')
        self.assertEqual(resolve(url).func, views.profile)

    def test_show_message(self):
        url = reverse('posts:message')
        self.assertEqual(resolve(url).func, views.show_message)
    
    def test_welcome(self):
        url = reverse('posts:welcome')
        self.assertEqual(resolve(url).func, views.welcome)
    
    def test_approve_open(self):
        url = reverse('posts:approve_open', args=[1])
        self.assertEqual(resolve(url).func, views.approve_open)
    
    def test_reject(self):
        url = reverse('posts:reject', args=[1])
        self.assertEqual(resolve(url).func, views.reject)
    
    def test_approve_change(self):
        url = reverse('posts:approve_change', args=[1])
        self.assertEqual(resolve(url).func, views.approve_change)

    def test_approve_clsoe(self):
        url = reverse('posts:approve_close', args=[1])
        self.assertEqual(resolve(url).func, views.approve_close)