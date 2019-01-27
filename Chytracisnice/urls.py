from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('contacts/', include('contacts.urls')),
    path('cookies', views.cookies, name='cookies'),
]
