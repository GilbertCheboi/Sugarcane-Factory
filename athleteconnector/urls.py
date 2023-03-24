"""tweetme2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include # url()
from django.views.generic import TemplateView

# from accounts.views import RegisterAPI
# from knox import views as knox_views
# from accounts.views import LoginAPI
# from django.urls import path



urlpatterns = [
    path('', include('Search.urls')),
    path('api/', include('Accounts.api.urls')),
    path('api/events/', include('Events.api.urls')),
    path('premium/', include('GoPremium.urls')),
    path('api/dm/', include('DirectMessaging.api.urls')),
    path('api/feed/', include('Feed.api.urls')),
    path('admin/', admin.site.urls),
    path('react/', TemplateView.as_view(template_name='react.html')),
    re_path(r'profiles?/', include('Profiles.urls')),
    # path('api/accounts/', include('Accounts.api.urls')),
    re_path(r'api/profiles?/', include('Profiles.api.urls')),
    path('api/profiles/', include('Profiles.api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                document_root=settings.MEDIA_ROOT)