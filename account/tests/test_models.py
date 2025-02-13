from django.test import TestCase
from account.models import Account, MessageFromEmployee, MessageFromThird, MessageFromUser, Check, Redem, CustomUser
from bank.models import Bank
class TestModels(TestCase):
    def setUp(self):
            pass