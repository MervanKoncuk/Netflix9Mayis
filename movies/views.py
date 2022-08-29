from django.shortcuts import render
from .models import *
from user.models import *
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
def index(request):
    populer = Movie.objects.filter(kategori__isim = 'Popüler')
    context = {
        'populer': populer
    }
    return render(request, 'index.html', context)
def movies(request, id):
    gundem = Movie.objects.filter(kategori__isim = 'Gündemde')
    populer = Movie.objects.filter(kategori__isim = 'Popüler')
    user = Profile.objects.get(id = id)
    context = {
        'gundem':gundem,
        'populer':populer,
        'profil':user
    }
    return render(request, 'browse-index.html', context)

def search(request):
    populer = Movie.objects.filter(kategori__isim = 'Popüler')
    movies = ''
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        movies = Movie.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    context = {
        'movies':movies,
        'search':search,
        'populer':populer
    }
    return render(request, 'search.html', context)

def detail(request):
    return render(request, 'detail.html')
