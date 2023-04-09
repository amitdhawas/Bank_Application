from django.urls import path

from transaction import views


urlpatterns = [
    path('deposite/',views.DepositeView.as_view(),name='deposite'),
    path('withdrawal/',views.WithdrawalView.as_view(),name='withdrawal'),
    path('transfer/',views.TransferVeiw.as_view(),name='transfer'),
    path('history/',views.BalenceHistory.as_view(),name='history'),

]


