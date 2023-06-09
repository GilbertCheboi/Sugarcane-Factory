from django.db import models

# Create your models here.
class STKPushResponse(models.Model):
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=100)
    response_code = models.CharField(max_length=100)
    response_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class PaymentDetails(models.Model):
    phone_number = models.IntegerField(max_length=10, null=False, blank=False)