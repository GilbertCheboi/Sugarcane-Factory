from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers import EventCreateSerializer
from ..models import Event
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def admin_index(request):
    return render(request)

# Create your views here.
@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def event_create_view(request, *args, **kwargs):
    '''
    Create an event (admin only)
    '''
    parser_classes = [MultiPartParser, FormParser]

    serializer = EventCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET']) 
# @permission_classes([IsAuthenticated])
def all_events(request, *args, **kwargs):
    '''
    See all events created by the admin
    '''
    events = Event.objects.all()
    serialize_events = EventCreateSerializer(events, many=True)
    
    return Response(serialize_events.data)

class SearchEventView(generics.ListAPIView):
    '''
    Search for an event
    '''
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['description']
    filterset_fields = ['id']
    ordering_fields = ['id']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Program
from ..serializers import ProgramCreateSerializer

# views.py
@api_view(['GET'])
def message_list(request):
    messages = Program.objects.all()
    serializer = ProgramCreateSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def message_create(request):
    serializer = ProgramCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def message_detail(request, pk):
    message = get_object_or_404(Program, pk=pk)
    serializer = ProgramCreateSerializer(message)
    return Response(serializer.data)

@api_view(['PUT'])
def message_update(request, pk):
    message = get_object_or_404(Program, pk=pk)
    serializer = ProgramCreateSerializer(message, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def message_delete(request, pk):
    message = get_object_or_404(Program, pk=pk)
    message.delete()
    return Response(status=204)
