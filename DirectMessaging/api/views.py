from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Message
from ..serializers import MessageSerializer

# views.py
@api_view(['GET'])
def message_list(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def message_create(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    serializer = MessageSerializer(message)
    return Response(serializer.data)

@api_view(['PUT'])
def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    serializer = MessageSerializer(message, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return Response(status=204)
