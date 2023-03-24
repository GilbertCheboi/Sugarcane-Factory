from rest_framework import serializers
from . models import Event, Program
from django.contrib.humanize.templatetags.humanize import naturaltime

class EventCreateSerializer(serializers.ModelSerializer):
    # time = serializers.DateField(input_formats=['%m-%d-%Y'])

    class Meta:
        model = Event
        fields = [
            # 'user', 
            # 'id', 
            'title',
            'image', 
            # 'video', 
            'description',
            'time',
            'timestamp'
            ]
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] = naturaltime(instance.timestamp)
        return representation


class ProgramCreateSerializer(serializers.ModelSerializer):
    # time = serializers.DateField(input_formats=['%m-%d-%Y'])

    class Meta:
        model = Program
        fields = [
            'name',
            'start', 
            'end',
            'products',
            ]
    

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['timestamp'] = naturaltime(instance.timestamp)
    #     return representation
