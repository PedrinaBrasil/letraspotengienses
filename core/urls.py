from django.urls import path, include
from core import views

app_name='core'

urlpatterns = [
    path('galeria/', views.gallery, name='gallery'),
    path('', views.home, name='home'),
    path('about', views.about, name='about')
]