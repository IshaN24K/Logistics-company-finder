from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Port(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.city.name})"

class Company(models.Model):
    COMPANY_TYPES = [
        ('LINE', 'Shipping Line'),
        ('NVOCC', 'NVOCC'),
    ]
    
    name = models.CharField(max_length=200)
    company_type = models.CharField(max_length=10, choices=COMPANY_TYPES)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    ports = models.ManyToManyField(Port, related_name="companies")

    def __str__(self):
        return self.name