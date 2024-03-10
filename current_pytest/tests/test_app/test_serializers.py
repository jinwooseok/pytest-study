import pytest
from rest_framework.fields import CharField
from app1.serializers import CurrencySerializer, UnfilledTransactionSerializer, FilledTransactionSerializer

class TestCurrencySerializer:

    transaction = UnfilledTransactionFactory.build()

    @pytest.mark.unit
    def test_serialize_model(self):
        currency = CurrencyFactory.build()
        serializer = CurrencySerializer(currency)

        assert serializer.data

    @pytest.mark.unit
    def test_serialized_data(self, mocker):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=CurrencyFactory
        )

        serializer = CurrencySerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert serializer.errors == {}


class TestUnfilledTransactionSerializer:

    @pytest.mark.unit
    def test_serialize_model(self):
        t = UnfilledTransactionFactory.build()
        expected_serialized_data = {
            'name': t.name,
            'currency': t.currency.code,
            'email': t.email,
            'amount_in_cents': t.amount_in_cents,
            'message': t.message,
        }

        serializer = UnfilledTransactionSerializer(t)

        assert serializer.data == expected_serialized_data
https://docs.pytest.org/en/stable/flaky.html
    @pytest.mark.django_db
    def test_serialized_data(self, mocker):
        c = CurrencyFactory()
        t = UnfilledTransactionFactory.build(currency=c)
        valid_serialized_data = {
            'name': t.name,
            'currency': t.currency.code,
            'email': t.email,
            'amount_in_cents': t.amount_in_cents,
            'message': t.message,
        }

        serializer = UnfilledTransactionSerializer(data=valid_serialized_data)

        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}

ml_model_name_max_chars = 134

    @pytest.mark.parametrize("wrong_field", (
        {"name": "a" * (ml_model_name_max_chars + 1)},
        {"tags": "tag outside of array"},
        {"tags": ["--------wrong length tag--------"]},
        {"version": "wronglengthversion"},
        {"is_public": 1},
        {"is_public": "Nope"},
    ))
    def test_deserialize_fails(self, wrong_field: dict):
        transaction_fields = [field.name for field in UnfilledTransaction._meta.get_fields()]
        invalid_serialized_data = {
            k: v for (k, v) in self.transaction.__dict__.items() if k in transaction_fields and k != "id"
        } | wrong_field

        serializer = MLModelSerializer(data=invalid_serialized_data)

        assert not serializer.is_valid()
        assert serializer.errors != {}

class TestFilledTransactionSerializer:

    @pytest.mark.unit
    def test_serialize_model(self, ftd):
        t = FilledTransactionFactory.build()
        expected_serialized_data = ftd(t)

        serializer = FilledTransactionSerializer(t)

        assert serializer.data == expected_serialized_data

    @pytest.mark.unit
    def test_serialized_data(self):
        t = FilledTransactionFactory.build()
        valid_serialized_data = {
            'id': t.id.hashid,
            'name': t.name,
            'currency': t.currency.code,
            'creation_date': t.creation_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'payment_date': t.payment_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'stripe_response': t.stripe_response,
            'payment_intent_id': t.payment_intent_id,
            'billing_name': t.billing_name,
            'billing_email': t.billing_email,
            'payment_status': t.payment_status,
            'link': t.link,
            'email': t.email,
            'amount_in_cents': t.amount_in_cents,
            'message': t.message,
        }

        serializer = FilledTransactionSerializer(data=valid_serialized_data)

        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}