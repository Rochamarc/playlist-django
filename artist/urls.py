from django.urls import path 

from . import views

urlpatterns = [
    path('songs/',views.index, name='index'),
    path('top/', views.top_index, name='top-index'),
    path('bands/',views.bands_index, name='bands-index'),
    path('band/<int:pk>',views.band_detail, name='band-detail'),
]