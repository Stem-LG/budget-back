from django.urls import path
from . import views


urlpatterns = [
    path("sayhi/",views.getHello)
]
