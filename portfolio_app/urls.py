from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'portfolio_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('About_me/', views.About_me, name='About_me'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('Blog/', views.Blog, name='Blog'),
    path('contact/', views.contact, name='contact'),
    
]