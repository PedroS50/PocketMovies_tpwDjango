from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    years_active = models.CharField(max_length=2)
    nationality = models.CharField(max_length=50)
    ##twitter account?
    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return self.name