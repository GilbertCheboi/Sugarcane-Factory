from django.urls import path
# from .views import MessageList, MessageDetail
from .views import(
    message_create,
    message_list, 
    message_detail, 
    message_update,
    message_delete,
)
urlpatterns = [
    path('create_message/', message_create, name='create_message'),
    path('see_all_messages/', message_list, name='create_message'),
    path('single_message/<int:pk>/', message_detail, name='create_message'),
    path('update_message/<int:pk>/', message_update, name='create_message'),
    path('delete_message/<int:pk>/', message_delete, name='create_message'),
]
