from django.shortcuts import render
from .models import Transaction, Entry

def index(request):
    return render(request, 'budget_app/index.html')

def transactions(request):
    all_transactions = Transaction.objects.all()
    return render(request, 'budget_app/transactions.html', {'transactions': all_transactions})

def transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    entries = Entry.objects.filter(transaction=transaction)
    return render(request, 'budget_app/transaction.html', {'transaction': transaction, 'entries': entries})

