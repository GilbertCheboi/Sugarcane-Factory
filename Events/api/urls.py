from django.urls import path
from django.views.generic import TemplateView

from .views import (
    event_create_view,
    all_events,
    admin_index,
    message_list,
    message_create,
)

from .views import SearchEventView
# from .views import SearchTweetView

'''
CLIENT
Base ENDPOINT /api/tweets/
'''
urlpatterns = [
    path('', SearchEventView.as_view()),
    path('create/', event_create_view),
    path('all_events/', all_events),
    path('django-admin/', TemplateView.as_view(template_name='admin.html')),
    path('events/', message_list),
    path('createvnt/', message_create),
] 