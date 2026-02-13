from django.urls import path, include
from . import views

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/profile/', views.profile_page, name ='profile-page'),
    path('login/', views.login_page, name = 'login-page'),
    path('logout/', views.logout_page, name = 'logout-page'),
    path('register/', views.register_page, name = 'register-page'),
]