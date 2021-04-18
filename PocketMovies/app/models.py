from django.db import models
from django.contrib.auth.models import User


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


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Director(models.Model):
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50)
    birthdate = models.DateField()
    website = models.URLField()


class Movie(models.Model):
    description = models.CharField(max_length=300)
    rating = models.FloatField()
    director = models.ManyToManyField(Director)
    producer = models.ManyToManyField(Producer)
    cast = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)


class Profile(models.Model):
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, null=True)
    favorite_genres = models.ManyToManyField(Genre, blank=True, null=True)
    favorite_movies = models.ManyToManyField(Movie, blank=True, null=True)
    movies_watched = models.ManyToManyField(Movie, blank=True, null=True)
    want_to_watch = models.ManyToManyField(Movie, blank=True, null=True)


