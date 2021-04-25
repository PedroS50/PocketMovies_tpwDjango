from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Director(models.Model):
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50)
    birthdate = models.DateField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50, default="Undefined")
    description = models.CharField(max_length=300)
    rating = models.FloatField()
    director = models.ManyToManyField(Director)
    producer = models.ManyToManyField(Producer)
    cast = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_picture = models.ImageField(blank=True)
    favorite_genres = models.ManyToManyField(Genre)
    favorite_movies = models.ManyToManyField(Movie, related_name='user_favorite_movies')
    movies_watched = models.ManyToManyField(Movie, related_name='user_watched_movies')
    want_to_watch = models.ManyToManyField(Movie, related_name='user_wanttowatch_movies')

    def __str__(self):
          return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
