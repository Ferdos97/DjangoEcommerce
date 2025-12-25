
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('store/', views.store_page),
    path('card/', views.card_page),
    path('about-us/', views.about_us_page),
    path('contact-us/', views.contact_us_page),
    path('form-submitted/', views.form_submitted_page),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #---> for static urls