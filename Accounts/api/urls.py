from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views

from .views import (
    RegisterAPI,
    LoginAPI,

)

from .views import (
    getall,
)


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('users/', getall, name='logout'),
]