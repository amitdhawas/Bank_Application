from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class AdminTtra(admin.ModelAdmin):
    list_display = ['account','ammount','balence_after_transaction','transaction_type','transfer_to','time']
