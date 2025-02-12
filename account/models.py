from django.db import models
from users.models import CustomUser,Employee
from bank.models import Bank

class Account(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    user_number = models.IntegerField(default=0, null=True, blank=True)


class MessageFromUser(models.Model):
    user_from = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True, related_name="sent_messages_from_user")
    user_to = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True, related_name="received_messages_from_employee")
    message = models.CharField(max_length=300, blank=True, null=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    user_number = models.IntegerField(default=0, null=True, blank=True)


class MessageFromEmployee(models.Model):
    user_from = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True, related_name="sent_messages_from_employee")
    user_to = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True,related_name="received_messages_from_user")
    message = models.CharField(max_length=300, blank=True, null=True)
    user_number = models.IntegerField(default=0, null=True, blank=True)


