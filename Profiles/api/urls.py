from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    profile_detail_api_view,
    profile_update_view,
    tweet_list_view,
    profile_create_view,
    all_profiles,
)

from .views import UpdateUserProfileView, GetUserProfileView, UserListView
'''
CLIENT
Base ENDPOINT /api/profiles/
'''
urlpatterns = [
    path('profile/', profile_create_view),
    path('allprofiles/', all_profiles),
    path('user-profile/', GetUserProfileView.as_view()),
    path('update-profile/', UpdateUserProfileView.as_view()),
    path('search-users/', UserListView.as_view()),

    path('<str:username>/', profile_detail_api_view),
    path('<str:username>/list', tweet_list_view),
    path('<str:username>/follow', profile_detail_api_view),
    path('<str:username>/edit', profile_update_view),   
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                document_root=settings.MEDIA_ROOT)