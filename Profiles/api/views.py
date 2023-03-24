import profile
import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
#from django.utils.http import is_safe_url
from rest_framework import generics, filters

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from ..models import Profile, Academics, Training
from rest_framework.views import APIView
from ..serializers import ProfileSerializer, PublicProfileSerializer, TrainingCreateSerializer
User = get_user_model()

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile_detail_view(request, username, *args, **kwargs):
#     current_user = request.user
#     to_follow_user = ??
#     return Response({}, status=200)
@api_view(['GET', 'POST'])
def profile_update_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "Username not found"}, status=404)
    profile = qs.first()
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer (profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def profile_detail_api_view(request, username, *args, **kwargs):
    # get the profile for the passed username
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "User not found"}, status=404)
    profile_obj = qs.first()
    data = request.data or {}
    if request.method == "POST":
        me = request.user
        action = data.get("action")
        if profile_obj.user != me:
            if action == "follow":
                profile_obj.followers.add(me)
            elif action == "unfollow":
                profile_obj.followers.remove(me)
            else:
                pass
    serializer = PublicProfileSerializer(instance=profile_obj, context={"request": request})
    return Response(serializer.data, status=200)

def get_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = PublicProfileSerializer(paginated_qs, many=True, context={"request": request})
    return paginator.get_paginated_response(serializer.data) 

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Profile.objects.all()
    username = request.GET.get('username') # ?username=Justin
    if username != None:
        qs = qs.by_username(username)
    return get_paginated_queryset_response(qs, request)

@api_view(['POST']) 
# @permission_classes([IsAuthenticated])
def profile_create_view(request, *args, **kwargs):
    '''
    Create an your profile
    '''

    serializer = PublicProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET']) 
# @permission_classes([IsAuthenticated])
def all_profiles(request, *args, **kwargs):
    '''
    See all events created by the admin
    '''
    events = Profile.objects.all()
    serialize_events = PublicProfileSerializer(events, many=True)
    
    return Response(serialize_events.data)

@permission_classes([IsAuthenticated])
class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        # try:
            user = self.request.user
            username = user.username

            data = self.request.data
            
            First_Name = data['First_Name']
            Last_Name = data['Last_Name']
            image = data['image']
            #Afcon = data['Afcon']
            # Baseball = data['Baseball']
            # Bundesliga = data['Bundesliga']
            # Europa = data['Europa']
            # Formula1 = data['Formula1']
            # Laliga = data['Laliga']
            # NBA = data['NBA']
            # NFL = data['NFL']
            # Worldcup = data['Worldcup']
            bio = data['bio']
            location = data['location']
            

            user = User.objects.get(id=user.id)
            Profile.objects.filter(user=user).update(
            image=image, 
            First_Name = First_Name,
            Last_Name = Last_Name,
             #   Afcon=Afcon, 
            #     Baseball=Baseball,
            #  Bundesliga=Bundesliga,
            #   Europa=Europa, 
            #   Formula1=Formula1,
            #    Laliga=Laliga, 
            #    NBA=NBA, 
            #    NFL=NFL, 
            #    Worldcup=Worldcup,
                bio=bio, 
                location=location
                )

            user_profile = Profile.objects.get(user=user)

            user_profile_serializer = PublicProfileSerializer(user_profile)
            return Response({'profile': user_profile_serializer.data, 'username': str(username)})
        
        # except:
        #     return Response({'error': 'Something went wrong when trying to update user profile.'})


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        # try:
            user = self.request.user
            username = user.username
            user = User.objects.get(id=user.id)
            user_profile = Profile.objects.get(user=user)

            user_profile_serializer = ProfileSerializer(user_profile)
            return Response({'profile': user_profile_serializer.data, 'username': str(username)})
        # except:
        #     return Response({'error': 'Error occurred when trying to get user profile'})

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = TrainingCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
