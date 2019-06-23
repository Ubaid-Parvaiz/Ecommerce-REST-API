"""practice_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from accounts.api import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('buyer.api.urls' , namespace = "api")),
    url(r'^api/token/',include('accounts.api.urls' , namespace = "api_token")),
    url(r'^api/user/',include('accounts.api.user.urls' , namespace = "api_users")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)