from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
	name = models.CharField(max_length=32)

class User(models.Model):
	user_details = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField(blank=True, null=True)
	favorite_genres = models.ManyToManyField(Genre, blank=True, null=True)
	favorite_movies = models.ManyToManyField(Movie, blank=True, null=True)
	movies_watched = models.ManyToManyField(Movie, blank=True, null=True)
	want_to_watch = models.ManyToManyField(Movie, blank=True, null=True)
	