from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us/', views.about_us),
    path('contact-us/', views.contact_us),
]