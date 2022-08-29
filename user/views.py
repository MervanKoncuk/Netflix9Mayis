from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.
def userRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Bu kullanıcı adı alınmış.')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Bu email alınmış.')
                return redirect('register')
            elif len(password) < 6:
                messages.error(request, "Şifreniz en az 6 karakter olması gerekiyor")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, first_name = firstName, last_name = lastName, email = email, password = password)
                user.save()
                messages.success(request, 'Kullanıcı oluşturuldu..')
                return redirect('login')
       
    return render(request, 'register.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yaptınız')
            return redirect('profiller')
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı")
            return redirect("login")
    return render(request, 'login.html')

def profiles(request):
    profiles = Profile.objects.filter(anaHesap = request.user).order_by('-isim')[:4]
    context = {
        'profiles': profiles
    }
    return render(request, 'browse.html', context)

def olustur(request):
    print("Deneme")
    print(Profile.objects.filter(anaHesap = request.user).count())
    if request.method == 'POST':
        isim = request.POST['isim']
        resim = request.FILES['resim']
        user = request.user
        
        if Profile.objects.filter(anaHesap = request.user).count() < 4:
            profile = Profile.objects.create(anaHesap = request.user, isim = isim, resim = resim)
            profile.save()
            messages.success(request, 'Profil oluşturuldu')
            return redirect('profiller')
        else:
            messages.error(request, 'En fazla 4 tane oluşturabilirsiniz. Daha fazla oluşturmak için Neos Yazılıma üye olun')
            return redirect('olustur')
    
    return render(request, 'profilOlustur.html')

def hesap(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'hesap.html', context)

def userLogout(request):
    logout(request)
    return redirect('index')

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Kullanıcı silindi')
    return redirect('index')