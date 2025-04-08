from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transactions/', views.transactions, name='transactions'),
    path('transaction/<int:transaction_id>/', views.transaction, name='transaction'),
]