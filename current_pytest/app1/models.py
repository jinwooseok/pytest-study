# inside apps/app/models.py

import string

from django.db import models
from django.utils import timezone
from hashid_field import HashidAutoField
from django.conf import settings

class Currency(models.Model):
    """Currency model"""
    name    = models.CharField(max_length=120, null=False, blank=False, unique=True)
    code    = models.CharField(max_length=3, null=False, blank=False, unique=True)
    symbol  = models.CharField(max_length=5, null=False, blank=False, default='$')

    def __str__(self) -> str:
        return self.code


class Transaction(models.Model):
    """Transaction model."""
    id                  = HashidAutoField(primary_key=True, min_length=8, alphabet=string.printable.replace('/', ''))
    name                = models.CharField(max_length=50, null=False, blank=False)
    email               = models.EmailField(max_length=50, null=False, blank=False)
    creation_date       = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    currency            = models.ForeignKey(Currency, null=False, blank=False, default=1, on_delete=models.PROTECT)
    payment_status      = models.Choices('PENDING', 'PAID', 'FAILED')
    payment_intent_id   = models.CharField(max_length=100, null=True, blank=False, default=None)
    message             = models.TextField(null=True, blank=True)

    @property
    def link(self):
        """
        Link to a payment form for the transaction
        """
        return settings.ALLOWED_HOSTS[0] + f'/payment/{str(self.id)}'