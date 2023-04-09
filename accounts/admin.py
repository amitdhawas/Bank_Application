from django.contrib import admin
from .models import UserBankAccount,UserAddress


@admin.register(UserAddress)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user','street_address','city','postal_code','country']

@admin.register(UserBankAccount)
class UserBankAdmin(admin.ModelAdmin):
    list_display = ['id','user','account_type','account_no','gender','birth_date','balence','initial_deposite_date']
