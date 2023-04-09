from django.db import models
from accounts.models import UserBankAccount
from transaction.constants import TRANSACTION_TYPE_CHOICES

# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount,on_delete=models.CASCADE)
    ammount = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    balence_after_transaction = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    transaction_type = models.CharField(max_length=50,choices=TRANSACTION_TYPE_CHOICES)
    transfer_to = models.PositiveIntegerField(null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)

    
