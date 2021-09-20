from django.db import models


# Create your models here.

class AuditoriaLead(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    lastname = models.CharField(max_length=120, null=True, blank=True)
    company = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    company_size = models.CharField(max_length=120, null=True, blank=True)
    role = models.CharField(max_length=120, null=True, blank=True)
    results = models.TextField(max_length=500, null=True, blank=True)

    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
