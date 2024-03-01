"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("band/", views.band_list, name="band-list"),
    path('band/<int:band_id>/', views.band_detail, name='band-detail'),
    path('band/<int:band_id>/edit/', views.band_edit, name='band-edit'),
    path('band/<int:band_id>/delete/', views.band_delete, name='band-delete'),
    path('band/add/', views.band_create, name='band-create'),
    path('about-us/', views.about, name='about'),
    path('listing/', views.listing_list, name='listing-list'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing-detail'),
    path('listing/add/', views.listing_create, name='listing-create'),
    path('listing/<int:listing_id>/edit/', views.listing_edit, name='listing-edit'),
    path('listing/<int:listing_id>/delete/', views.listing_delete, name='listing-delete'),
    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='email-sent'),
]
