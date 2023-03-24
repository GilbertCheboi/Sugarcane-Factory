from rest_framework import serializers
from .models import Message
from django.contrib.humanize.templatetags.humanize import naturaltime
# from django.conf import settings
from django.contrib.auth.models import User

# User = settings.AUTH_USER_MODEL


# serializers.py
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class MessageSerializer(serializers.ModelSerializer):
    # sender = UserSerializer()
    # receiver = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'message', 'created_at')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = naturaltime(instance.created_at)
        return representation