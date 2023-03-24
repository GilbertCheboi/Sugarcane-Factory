from django.urls import path

from .views import (
MakePayment,
)
from .views import Access_token, GenereatedPasswordView
'''
CLIENT
Base ENDPOINT /api/tweets/
'''
urlpatterns = [
    path('safaricom_token/', Access_token.as_view()),
    path('safaricom_password/', GenereatedPasswordView.as_view()),
    # path('', SearchTweetView.as_view()),
    path('pay/', MakePayment),
]
