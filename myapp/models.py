from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    ptc = models.CharField(max_length=100)
    email = models.EmailField()
    contact_nos = models.CharField(max_length=50)
    specialities = models.ManyToManyField(Service)

    def __str__(self): return self.name