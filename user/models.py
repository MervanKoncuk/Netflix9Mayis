from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    anaHesap = models.ForeignKey(User, on_delete = models.CASCADE, null=True) # models.SET_NULL
    isim = models.CharField(max_length=50)
    resim = models.FileField(upload_to = 'profiles/', verbose_name='Profil Resmi')

    def __str__(self):
        return self.isim