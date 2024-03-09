'''Description: app1의 views를 정의하는 파일'''
from rest_framework.viewsets import ModelViewSet
from app1.models import Transaction, Currency
from app1.serializers import TransactionSerializer, CurrencySerializer, UnfilledTransactionSerializer, FilledTransactionSerializer

class CurrencyViewSet(ModelViewSet):
    '''Currency 모델에 대한 viewset'''
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    
    
class TransactionViewSet(ModelViewSet):
    '''Transaction 모델에 대한 viewset'''
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def get_serializer_class(self):
        '''serializer_class를 동적으로 변경'''
        if self.action == 'create':
            return UnfilledTransactionSerializer
        else:
            return FilledTransactionSerializer