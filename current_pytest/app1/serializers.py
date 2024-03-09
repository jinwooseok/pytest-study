from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers

from django.conf import settings
from django.core.validators import MaxLengthValidator, ProhibitNullCharactersValidator
from rest_framework.validators import ProhibitSurrogateCharactersValidator

from app1.models import Currency, Transaction


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'code', 'symbol']
        if settings.DEBUG == True:
            extra_kwargs = {
                'name': {
                    'validators': [MaxLengthValidator, ProhibitNullCharactersValidator]
                },
                'code': {
                    'validators': [MaxLengthValidator, ProhibitNullCharactersValidator]
                }
            }

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class UnfilledTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(
        slug_field='code',
        queryset=Currency.objects.all(),
    )

    class Meta:
        model = Transaction
        fields = (
            'name',
            'currency',
            'email',
            'amount_in_cents',
            'message'
        )

class FilledTransactionSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field='transaction.Transaction.id', read_only=True)
    currency = serializers.StringRelatedField(read_only=True)
    link = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {
            """Non editable fields"""
            'id': {'read_only': True},
            'creation_date': {'read_only': True},
            'payment_date': {'read_only': True},
            'amount_in_cents': {'read_only': True},
            'payment_intent_id': {'read_only': True},
            'payment_status': {'read_only': True},

        }