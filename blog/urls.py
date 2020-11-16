from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
   
     path('', views.home, name='home'),
     path('blog/', views.blog, name='blog'),
     path('contact/', views.contact, name='contact'),
     path('search/',views.search, name='search'),
     path('blogpost/<str:slug>', views.blogpost, name='blogpost')
]
