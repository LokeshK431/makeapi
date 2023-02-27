from django import views
from django.urls import path
from django.contrib import admin
import sys
sys.path.append("...restfulapi/views.py")
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    
]