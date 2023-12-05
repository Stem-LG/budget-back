from django.urls import path
from . import views


urlpatterns = [
    path(r'login/',views.login),
    path(r'register/',views.register),
    path(r'logout/',views.logout),
    path(r'test_token/',views.test_token),
    ]