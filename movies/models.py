from tabnanny import verbose
from django.db import models

# Create your models here.s
class Kategori(models.Model):
    isim = models.CharField(max_length=50)

    def __str__(self):
        return self.isim

class Movie(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=50, verbose_name='Film adı')
    resim = models.FileField(upload_to='filmler/', null=True, verbose_name="Filmler")

    def __str__(self):
        return self.isim