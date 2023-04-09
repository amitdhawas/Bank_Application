from django.shortcuts import render,redirect
from django.conf import settings
from .models import UserBankAccount,UserAddress
from .forms import UserForm,AccountForm,UserAddressForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from django.contrib.auth.models import User

class UserView(TemplateView):
    model = User
    template_name = 'accounts/home.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)   
        form_class = UserForm
        data = User.objects.all()
        context = {'form':form_class,'data':data}
        return context
    
    def post(self,request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('address')
    

class AccountCreateView(TemplateView):
    model = UserBankAccount
    template_name = 'accounts/account.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)   
        form_class = AccountForm
        data = UserBankAccount.objects.all()
        context = {'form':form_class,'data':data}
        return context
    
    def post(self,request):
        form = AccountForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            ac = form.cleaned_data['account_type']
            accno = (
                    user.id +
                    settings.ACCOUNT_NUMBER_START_FROM
                )
            gn = form.cleaned_data['gender']
            bd = form.cleaned_data['birth_date']
            bl = form.cleaned_data['balence']
            dd = form.cleaned_data['initial_deposite_date']
            obj = UserBankAccount(user=user,account_type=ac,account_no=accno,gender=gn,birth_date=bd,balence=bl,initial_deposite_date=dd)
            obj.save()
        return redirect('dashboard')

class UserAddressView(CreateView):
    model = UserAddress
    form_class = UserAddressForm
    template_name = 'accounts/address.html'
    success_url = '/accounts/account/'

class UserNameDetails(DetailView):
    model = User
    template_name = 'accounts/namedetails.html'
    context_object_name = 'details'


def CustomerDetails(request):
    user = request.user
    data = UserBankAccount.objects.get(user=user)
    return render(request,'accounts/details.html',{'details':data})

class CustomerAddressDetails(DetailView):
    model = UserAddress
    template_name = 'accounts/customeraddressdetails.html'
    context_object_name = 'details'


