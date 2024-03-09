'''make fixture'''
import pytest
from rest_framework.test import APIClient
from factories import TransactionBakery, CurrencyBakery

@pytest.fixture
def ftbp():
    '''filled_transaction_bakery'''
    def filled_transaction_bakery(n=1):
        param = {
            'amount_in_cents':1032000, # --> Passes min. payload restriction in every currency
            'currency':CurrencyBakery(n=n).prepare()
        }
        utb = TransactionBakery(add_param=param, n=n).prepare()
        return utb
    return filled_transaction_bakery

@pytest.fixture
def ftbm():
    '''filled_transaction_bakery'''
    def filled_transaction_bakery(n=1):
        param = {
            'amount_in_cents':1032000, # --> Passes min. payload restriction in every currency
            'currency':CurrencyBakery(n=n).make()
        }
        utb = TransactionBakery(add_param=param, n=n).make()
        return utb
    return filled_transaction_bakery

@pytest.fixture
def fcbp():
    '''filled_currency_bakery'''
    def filled_currency_bakery(n=1):
        '''Currency 모델 데이터 준비'''
        return CurrencyBakery(n=n).prepare()
    return filled_currency_bakery

@pytest.fixture
def fcbm():
    '''filled_currency_bakery'''
    def filled_currency_bakery(n=1):
        '''Currency 모델 데이터 생성'''
        return CurrencyBakery(n=n).make()
    return filled_currency_bakery

@pytest.fixture
def api_client():
    '''클라이언트 환경을 동일하게 맞추고 테스트하기 위한 fixture'''
    return APIClient
