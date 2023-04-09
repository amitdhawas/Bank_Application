from django.shortcuts import render,redirect
from django.conf import settings
from .models import Transaction
from .forms import TransactionForm
from django.views.generic import TemplateView,ListView
from accounts.models import UserBankAccount

# Create your views here.

class DepositeView(TemplateView):
    model = Transaction
    template_name = 'transaction/transactions.html'
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(*args,**kwargs)
        form_class = TransactionForm
        context = {'form':form_class,'msg':'Enter Details to Deopsite Moany'}
        return context

    def post(self,request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            account =  request.POST.get('account')
            data = UserBankAccount.objects.get(account_no=account)
            ammount = form.cleaned_data['ammount']
            tr = form.cleaned_data['transaction_type']
            if float(ammount) <= 0:
                context = {'msg':'Please Enter Valid Ammount'}
                return render(request,'transaction/exception.html',context)
            else:  
                UserBankAccount.objects.filter(account_no=account).update(balence=int(data.balence) + int(ammount))
                data = UserBankAccount.objects.get(account_no=account)
                obj = Transaction(account=data,ammount=ammount,balence_after_transaction=data.balence,transaction_type=tr)
                obj.save()
            return redirect('dashboard') 

class WithdrawalView(TemplateView):
    model = Transaction
    template_name = 'transaction/transactions.html'
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(*args,**kwargs)
        form_class = TransactionForm
        context = {'form':form_class,'msg':'Enter Details to Withdrawal Moany'}
        return context


    def post(self,request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            account =  request.POST.get('account')
            data = UserBankAccount.objects.get(account_no=account)
            ammount = form.cleaned_data['ammount']
            tr = form.cleaned_data['transaction_type']
            if float(ammount) <= 0:
                context = {'msg':'Please Enter Valid Ammount'}
                return render(request,'transaction/exception.html',context)
            elif float(ammount)+500 > float(data.balence):
                context = {'msg':'Insufficient fundes in your Account please check your balence'}
                return render(request,'transaction/exception.html',context)
            else:
                UserBankAccount.objects.filter(account_no=account).update(balence=int(data.balence) - int(ammount))
                data = UserBankAccount.objects.get(account_no=account)
                obj = Transaction(account=data,ammount=ammount,balence_after_transaction=data.balence,transaction_type=tr)
                obj.save()
            return redirect('dashboard') 

class TransferVeiw(TemplateView):
    model = Transaction
    template_name = 'transaction/transfer.html'
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(*args,**kwargs)
        form_class = TransactionForm
        context = {'form':form_class,'msg':'Enter Details to Transfer Moany'}
        return context

    def post(self,request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            account =  request.POST.get('account')
            taccount = request.POST.get('taccount')
            data = UserBankAccount.objects.get(account_no=account)
            tdata = UserBankAccount.objects.get(account_no=taccount)
            ammount = form.cleaned_data['ammount']
            tr = form.cleaned_data['transaction_type']
            if float(ammount) <= 0:
                context = {'msg':'Please Enter Valid Ammount'}
                return render(request,'transaction/exeption.html',context)
            elif float(ammount)+500 > float(data.balence):
                context = {'msg':'Insufficient fundes in your Account please check your balence'}
                return render(request,'transaction/exception.html',context)
            else:
                UserBankAccount.objects.filter(account_no=account).update(balence=int(data.balence) - int(ammount))
                UserBankAccount.objects.filter(account_no=taccount).update(balence=int(tdata.balence) + int(ammount))
                data = UserBankAccount.objects.get(account_no=account)
                obj = Transaction(account=data,ammount=ammount,balence_after_transaction=data.balence,transaction_type=tr,transfer_to=taccount)
                obj.save()
        return redirect('/') 


class BalenceHistory(ListView):
    model = Transaction
    template_name = 'transaction/history.html'
    context_object_name = 'history'




