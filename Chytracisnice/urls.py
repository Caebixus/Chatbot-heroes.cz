from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('contacts/', include('contacts.urls')),
    path('cookies', views.cookies, name='cookies'),
    path('restaurace_a_kavarny_chatbot_vzor', views.restfreevzor, name='restfreevzor'),
    path('realitni_makleri_chatbot_vzor', views.realitkyfreevzor, name='realitkyfreevzor'),
    path('blog1', views.blog1, name='blog1'),
]
