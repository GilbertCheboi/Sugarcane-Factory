from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Events.models import Event
from DirectMessaging.models import Message
from Profiles.models import Profile

from Events.serializers import EventCreateSerializer
from DirectMessaging.serializers import MessageSerializer
from Profiles.serializers import ProfileSerializer

@api_view(['GET'])
def search(request):
    query = request.GET.get('q')
    events = Event.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    messages = Message.objects.filter(message__icontains=query)
    profiles = Profile.objects.filter(Q(location__icontains=query) | Q(bio__icontains=query) | Q(age__icontains=query))
    # Add any other models you want to search across here...
    results =[
        {'model': 'Event', 'data': EventCreateSerializer(events, many=True).data},
        {'model': 'Message', 'data': MessageSerializer(messages, many=True).data},
        {'model': 'Profile', 'data': ProfileSerializer(profiles, many=True).data},
        # Add any other model serializers here...
    ]
    return Response(results)
