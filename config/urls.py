"""
URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve


urlpatterns = [
    path('cabinet/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('media/', views.static.serve),
    path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
