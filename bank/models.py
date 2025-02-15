from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=75)

    def __str__(self):
        return self.bank_name
    

class Change(models.Model):
    current_bank_name = models.CharField(max_length=100)
    new_bank_name = models.CharField(max_length=100)      
    user_number = models.IntegerField()

    
