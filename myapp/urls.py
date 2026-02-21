from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # Proxy endpoints for country/state data (server-side to protect API key)
    path('api/countries/', countries_api, name='api_countries'),
    path('api/countries/<str:country_code>/states/', states_api, name='api_states'),
    path('accounts/', include('django.contrib.auth.urls')), # Handles login/logout
    path('signup/', signup_view, name='signup'),
    path('', home, name='home'),
    path('add-company/', add_company, name='add_company'),
]