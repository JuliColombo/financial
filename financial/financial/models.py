from django.utils import timezone


class NegativeTransactionException(Exception):
    pass


class SimultaneousUpdateError(Exception):
    pass


class ConcurrencyMixin:

    def __init__(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def save_execute(self, func, args):
        if self.locked:
            raise SimultaneousUpdateError
        else:
            self.lock()
            func(args)
            self.unlock()


class Account(ConcurrencyMixin):

    def __init__(self):
        ConcurrencyMixin.__init__(self)
        self.balance = 0
        self.transactions = []

    def get_balance(self):
        return self.balance

    def debit(self, amount):
        return self.balance - amount

    def credit(self, amount):
        return self.balance + amount

    def charge_transaction(self, transaction):
        if transaction.type == 'debit':
            result = self.debit(transaction.amount)
        else:
            result = self.credit(transaction.amount)

        if result < 0:
            raise NegativeTransactionException()
        self.balance = result
        self.transactions.append(transaction)

    def make_transaction(self, transaction):
        self.save_execute(self.charge_transaction, transaction)


class Transaction:

    def __init__(self, type, amount):
        if not type in ('debit', 'credit'):
            raise Exception('Invalid transaction type')
        self.id = str(id(self))
        self.type = type
        self.amount = amount
        self.created_at = timezone.now()
