from django.urls import path
from . import views

urlpatterns=[
    path('', views.membership_options, name='membership_options'),
    path('upgrade/', views.upgrade_to_premium, name='upgrade_to_premium'),
     path('payment/', views.payment_gateway, name='payment_gateway'),
     path('transactions/', views.transaction_history, name='transaction_history'),
     
]