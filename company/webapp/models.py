from django.db import models

class Company(models.Model):
    cname=models.CharField(max_length=50)
    cemail=models.EmailField()
    city=models.CharField(max_length=200)
