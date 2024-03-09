#app1/urls.py
from . import views

route_list = [
    ('currencies', views.CurrencyViewSet),
    ('transactions', views.TransactionViewSet)
]
