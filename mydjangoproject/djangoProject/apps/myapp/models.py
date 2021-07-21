from django.db import models

# Create your models here.

class registrationModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
