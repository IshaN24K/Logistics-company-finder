from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # Handles login/logout
    path('signup/', signup_view, name='signup'),
    path('', home, name='home'),
    path('add-company/', add_company, name='add_company'),
]