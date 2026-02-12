from django.shortcuts import render
from django.contrib.auth import authenticate, login


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
    pass


def register_page(request):
    pass