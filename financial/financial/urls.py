from django.conf.urls import include, url

from financial.views import BalanceView, TransactionView, HistoryView

urlpatterns = [
    url(r'^balance/', BalanceView.as_view(), name='balance'),
    url(r'^transactions/(?P<id>[\w\-]+)/', TransactionView.as_view(), name='single_transaction'),
    url(r'^transactions/', TransactionView.as_view(), name='transactions'),
    url(r'^history/', HistoryView.as_view(), name='history'),
]
