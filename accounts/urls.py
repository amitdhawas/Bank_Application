from django.urls import path

from . import views


urlpatterns = [
    path('user',views.UserView.as_view(),name='userview'),
    path('account/',views.AccountCreateView.as_view(),name='account'),
    path('details/',views.CustomerDetails,name='details'),
    path('address/',views.UserAddressView.as_view(),name='address'),
    path('customerdetails/<int:pk>/',views.UserNameDetails.as_view(),name='namedetails'),
    path('customeraddressdetails/<int:pk>/',views.CustomerAddressDetails.as_view(),name='customeraddressdetails'),
]


