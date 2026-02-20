from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # This tells Django to include ALL fields from the model
        fields = '__all__'
        
        widgets = {
            'specialities': forms.SelectMultiple(attrs={'class': 'select2-multi'}),
            # We change these to Select widgets so the JS can fill them with options
            'country': forms.Select(attrs={'id': 'country-select'}),
            'state': forms.Select(attrs={'id': 'state-select'}),
            # You can also add classes to make text inputs look better
            'name': forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),
            'ptc': forms.TextInput(attrs={'placeholder': 'Point of Contact Name'}),
        }