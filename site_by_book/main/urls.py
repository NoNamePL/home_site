from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, login

urlpatterns = [
    path('', index, name='home'),
    path('login', login, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

