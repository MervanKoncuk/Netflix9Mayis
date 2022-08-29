from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('filmler/<int:id>', movies, name="movies"),
    path('arama/', search, name='search'),
]