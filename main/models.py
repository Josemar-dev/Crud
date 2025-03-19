from django.db import models

class menbro(models.Model):
    primeironome = models.CharField(max_length=100)
    segundonome = models.CharField(max_length=100)
    terceironome = models.CharField(max_length=100)