from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name='login'),
    path('profiller/', profiles, name='profiller'),
    path('olustur/', olustur, name='olustur'),
    path('hesap/', hesap, name="hesap"),
    path('logout/', userLogout, name="logout"),
    path('delete/', userDelete, name="delete"),
]