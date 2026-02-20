from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after signup
            return redirect('home') # Redirect to your home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Or redirect to a list view
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})


def find_company(request):
    services = Service.objects.all()
    results = Company.objects.all()
    
    # Filter by name
    name_query = request.GET.get('name')
    if name_query:
        results = results.filter(name__icontains=name_query)
        
    # Filter by multiple specialities
    selected_services = request.GET.getlist('specialities')
    if selected_services:
        results = results.filter(specialities__id__in=selected_services).distinct()

    return render(request, 'find_company.html', {
        'results': results, 
        'all_services': services
    })