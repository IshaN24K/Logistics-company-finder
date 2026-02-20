from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'specialities': forms.SelectMultiple(attrs={'class': 'select2-multi'}),
            'country': forms.Select(attrs={'id': 'country-select'}),
            'state': forms.Select(attrs={'id': 'state-select'}),
        }