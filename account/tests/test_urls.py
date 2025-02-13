from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import open_account, close_account, change_bank, send_check, redem_check
class TestUrls(SimpleTestCase):
    def test_open_account(self):
        url = reverse('account:open_account')
        self.assertEqual(resolve(url).func, open_account)
    
    def test_close_account(self):
        url = reverse('account:close_account')
        self.assertEqual(resolve(url).func, close_account)

    def test_change_bank(self):
        url = reverse('account:change_bank')
        self.assertEqual(resolve(url).func, change_bank)

    def test_send_check(self):
        url = reverse('account:send_check')
        self.assertEqual(resolve(url).func, send_check)

    def test_redem_check(self):
        url = reverse('account:redem_check')
        self.assertEqual(resolve(url).func, redem_check)