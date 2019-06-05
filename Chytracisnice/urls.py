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
    path('eshopy_chatbot_vzor', views.eshopyfreevzor, name='eshopyfreevzor'),
    path('5_kroku_k_vytvoreni_chatbota', views.blog1, name='blog1'),
    path('Jak_pridat_messenger_chatbot_na_web', views.blog2, name='blog2'),
    path('Chatbot-pro-eshopy-nabidne-nesplni', views.blog3, name='blog3'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
]
