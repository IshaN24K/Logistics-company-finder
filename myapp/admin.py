from django.contrib import admin
from .models import Service, Company

# Register models to allow admin management and seeding
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name', 'country', 'state', 'email')
	search_fields = ('name', 'country', 'state', 'email')
