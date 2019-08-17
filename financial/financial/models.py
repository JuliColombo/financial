from django.utils import timezone


class NegativeTransactionException(Exception):
    pass


class Account:

    def __init__(self):
        self.balance = 0
        self.transactions = []

    def get_balance(self):
        return self.balance

    def debit(self, amount):
        return self.balance - amount

    def credit(self, amount):
        return self.balance + amount

    def make_transaction(self, transaction):
        if transaction.type == 'debit':
            result = self.debit(transaction.amount)
        else:
            result = self.credit(transaction.amount)

        if result < 0:
            raise NegativeTransactionException()
        self.balance = result
        self.transactions.append(transaction)


class Transaction:

    def __init__(self, type, amount):
        if not type in ('debit', 'credit'):
            raise Exception('Invalid transaction type')
        self.id = str(id(self))
        self.type = type
        self.amount = amount
        self.created_at = timezone.now()
