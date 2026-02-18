from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'company_type', 'contact_person', 'phone', 'email', 'city', 'ports']
        # This makes the multi-select port list look better
        widgets = {
            'ports': forms.CheckboxSelectMultiple(),
        }