from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('registration', views.registration_form, name='registration_page'),
    path('login', views.login_form, name='login_page'),
    path('dashboard', views.dashboard, name='dashboard_page'),
    path('form', views.dashboard_form_data, name='dashboard_form'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='contact-page'),
]
