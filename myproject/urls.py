from django.contrib import admin
from django.urls import path
import wordcnt.views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', wordcnt.views.home, name='home'),
    path('about/', wordcnt.views.about, name='about'),
    path('result/', wordcnt.views.result, name='result'),
]
