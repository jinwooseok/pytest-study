import json
import pytest
from app1.models import Transaction, Currency

pytestmark = pytest.mark.django_db

class TestCurrencyEndpoints:

    endpoint = '/api/currencies/'

    def test_list(self, api_client, fcbm):
        fcbm(n=3)

        response = api_client().get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3
    
    def test_retrieve(self, api_client, fcbm):
        currency = fcbm(n=1)[0]
        expected_json = {
            'name': currency.name,
            'code': currency.code,
            'symbol': currency.symbol
        }
        url = f'{self.endpoint}{currency.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_create(self, api_client, fcbp):
        currency = fcbp()[0]
        request_data = {
            'name': currency.name,
            'code': currency.code,
            'symbol': currency.symbol
        }

        response = api_client().post(
            self.endpoint,
            data=request_data,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == request_data
                
    def test_update(self, api_client, fcbm, fcbp):
        old_currency = fcbm()[0]
        new_currency = fcbp()[0]
        request_data = {
            'code': new_currency.code,
            'name': new_currency.name,
            'symbol': new_currency.symbol
        }
        response = api_client().put(
            f'{self.endpoint}{old_currency.id}/',
            data = request_data,
            format='json'
        )

        assert response.status_code == 200
        assert Currency.objects.get(id=old_currency.id).name == new_currency.name