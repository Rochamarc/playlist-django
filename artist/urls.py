from django.urls import path 

from . import views

urlpatterns = [
    path('songs/',views.index, name='index'),
]