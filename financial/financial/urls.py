from django.conf.urls import include, url

from financial.views import BalanceView, TransactionView

urlpatterns = [
    url(r'^balance/', BalanceView.as_view(), name='home'),
    url(r'^transactions/(?P<id>[\w\-]+)/', TransactionView.as_view(), name='transactions'),
    url(r'^transactions/', TransactionView.as_view(), name='transactions'),
]
