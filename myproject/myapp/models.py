from django.db import models

class Kool(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Register(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=10) 

    def __str__(self):
        return self.name   
