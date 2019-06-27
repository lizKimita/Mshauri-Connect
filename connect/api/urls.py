from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from connect.api.views import LNMCallbackUrlAPIView

urlpatterns = [
    url(r'^lnm/', LNMCallbackUrlAPIView.as_view(), "lnm-CallBackURL"),


]
