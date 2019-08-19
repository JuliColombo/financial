import json
import os

from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from financial.models import Account, Transaction, NegativeTransactionException


account = Account()


def build_transaction_json(transaction):
    return {'id': transaction.id,
            'type': transaction.type,
            'amount': transaction.amount,
            'effectiveDate': transaction.created_at}


def transactions():
    transactions = []
    for transaction in account.transactions:
        transactions.append(build_transaction_json(transaction))
    return transactions


class BalanceView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Balance: ' + str(account.get_balance()))


class TransactionView(View):

    def get_by_id(self, id):
        found_transaction = next((t for t in account.transactions if t.id == id), None)
        if not found_transaction:
            return HttpResponse('Transaction not found', status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(build_transaction_json(found_transaction), status=status.HTTP_200_OK)

    def get_all(self):
        try:
            return JsonResponse(transactions(), status=status.HTTP_200_OK, safe=False)
        except Exception:
            return HttpResponse('Invalid status value', status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            return self.get_by_id(id)
        return self.get_all()

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        transaction = Transaction(type=data['type'], amount=data['amount'])
        try:
            account.make_transaction(transaction)
        except NegativeTransactionException:
            return HttpResponse('Cannot have negative balance', status=status.HTTP_400_BAD_REQUEST)
        except:
            return HttpResponse('Invalid input', status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(build_transaction_json(transaction), status=status.HTTP_200_OK)


class HistoryView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'transactions': transactions()})