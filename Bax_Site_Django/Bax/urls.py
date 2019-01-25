from django.urls import path
from . import views
from .views import emailView, successView
from django.contrib import admin

urlpatterns = [
    path('', views.Bax, name="home"),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
    ]
