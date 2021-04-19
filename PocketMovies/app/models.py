from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    name = models.CharField(max_length=64)


class Profile(models.Model):
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_picture = models.ImageField(blank=True)
    favorite_genres = models.ManyToManyField(Genre)
    favorite_movies = models.ManyToManyField(Movie, related_name='user_favorite_movies')
    movies_watched = models.ManyToManyField(Movie, related_name='user_watched_movies')
    want_to_watch = models.ManyToManyField(Movie, related_name='user_wanttowatch_movies')
# favorite_movies = models.ManyToManyField(Movie, through='FavoriteMovies')
# movies_watched = models.ManyToManyField(Movie, through='MoviesWatched')
# want_to_watch = models.ManyToManyField(Movie, through='WantToWatch')

# class FavoriteMovies(models.Model):
# 	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
# 	movie = models.ForeignKey(Profile, on_delete=models.CASCADE)

# class MoviesWatched(models.Model):
# 	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
# 	movie = models.ForeignKey(Profile, on_delete=models.CASCADE)

# class WantToWatch(models.Model):
# 	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
# 	movie = models.ForeignKey(Profile, on_delete=models.CASCADE)
