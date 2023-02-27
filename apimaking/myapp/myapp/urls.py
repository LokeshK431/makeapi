"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django import views
from django.urls import path
from django.contrib import admin
import sys
sys.path.append("/apimaking/restapi/restfulapi/views.py")
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
]

from django.urls import path
from django.contrib import admin
from restapi import views as restapi_views
from myapp import views as myapp_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'item', myapp_views.ItemViewSet, basename='item')
router.register(r'order', myapp_views.OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', restapi_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
