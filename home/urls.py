from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('project', views.project, name="project"),
    path('cycle', views.cycle, name="cycle"),
    path('dogo', views.dogo, name="doggo"),
    path('about', views.about, name="about"),
    path('notfound', views.notfound, name="notfound")
]
