from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # username & password come from: (names in login.html)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    if request.user.is_authenticated:
        return render(request, 'blog/index.html', {})
    else:
        return render(request, 'accounts/login.html', {})
    

def logout_page(request):
    return render(request, 'accounts/logout.html', {})


def register_page(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            return redirect('login-page')
    
    return render(request, 'accounts/register.html')


def profile_page(request):
    return redirect('home-page')
