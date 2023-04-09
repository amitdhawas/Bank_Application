from django import forms 
from .models import UserBankAccount,UserAddress,User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Enter Password Again',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',]
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        labels = {
            'email1':'Enter Email',
        }
    


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['user','street_address','city','postal_code','country']
        widgets = {
            'street_address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'postal_code':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            }
        
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserBankAccount
        fields = ['user','gender','account_type','birth_date','balence','initial_deposite_date']
        widgets = {
            'account_type':forms.TextInput(attrs={'class':'form-control'}),
            'birth_date':forms.TextInput(attrs={'class':'form-control'}),
            'balence':forms.TextInput(attrs={'class':'form-control'}),
            'initial_deposite_date':forms.TextInput(attrs={'class':'form-control'})
        }
        labels = {
            'birth_date':'Birth Date(yyyy-mm-dd)',
            'balence': 'Deposite Ammount',
            'initial_deposite_date': 'Date(yyyy-mm-dd)'

        }