from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_CHOICE

class UserAddress(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=100)

    


class UserBankAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100,help_text='Enter Account Type Current/Savings' )
    account_no = models.PositiveIntegerField(unique=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True,blank=True)
    balence = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    initial_deposite_date = models.DateField(null=True,blank=True)

    def __strt__(self):
        return self.user



