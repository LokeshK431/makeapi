from django.urls import path
from django.contrib import admin
from restapi import views as restapi_views
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', restapi_views.ContactAPIView.as_view()),
]