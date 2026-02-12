from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name = 'login-page'),
    path('logut/', views.logout_page, name = 'logout-page'),
    path('register/', views.register_page, name = 'register-page'),
]