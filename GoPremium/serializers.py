from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
# from django.conf import settings
# from django.contrib.auth.models import User
from .models import PaymentDetails

# User = settings.AUTH_USER_MODEL


# serializers.py
class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['phone_number']