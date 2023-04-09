from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

class UserLogoutView(LogoutView):
    template_name = 'registration/logout.html'


def Dashboard(request):
    user = request.user
    full_name = user.get_full_name()
    return render(request,'registration/home.html',{'full_name':full_name})
