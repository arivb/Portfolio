from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.homepage,name='home'),
    path('homepage',views.homepage,name='homepage'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('contacts',views.contacts,name='contacts'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('game',views.game,name='game')




]