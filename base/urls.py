from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cookies', views.cookies, name='cookies'),
]
