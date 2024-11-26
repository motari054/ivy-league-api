# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AccessToken(models.Model):
    token = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "created_at"

    def __str__(self):
        return self.token


class Payments(models.Model):
    merchant_request_id = models.CharField(max_length=255, unique=True)
    checkout_request_id = models.CharField(max_length=255, unique=True)
    receipt_number = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    result_code = models.IntegerField()
    result_desc = models.TextField()
    transaction_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.receipt_number} - {self.amount}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
