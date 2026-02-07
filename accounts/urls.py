from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name = 'login-page'),
    path('logut/', views.login_page, name = 'logout-page'),
    path('register/', views.login_page, name = 'register-page'),
]