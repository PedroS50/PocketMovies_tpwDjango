"""PocketMovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('movies/', views.list_movies, {'movie': 'all'}, name='ListMovies'),
    path('movies/my_favorite_movies/', views.list_movies, {'movie': 'my_favorite_movies'}, name='my_favorite_movies'),
    path('movies/my_want_to_watch/', views.list_movies, {'movie': 'my_want_to_watch'}, name='my_want_to_watch'),
    path('movies/my_watched_movies/', views.list_movies, {'movie': 'my_watched_movies'}, name='my_watched_movies'),
    path('actors/', views.list_people, {'person': 'actors'}, name='ListActors'),
    path('producers/', views.list_people, {'person': 'producers'}, name='ListActors'),
    path('directors/', views.list_people, {'person': 'directors'}, name='ListActors'),
    path('producer/<id>', views.infoProducer, name="infoProducer"),
    path('actor/<id>', views.infoActor, name="infoActor"),
    path('search/', views.searchMovie, name="searchMovie"),
    path('movie/<id>', views.infoMovie, name="infoMovie"),
    path('director/<id>', views.infoDirector, name="infoDirector"),
    path('add/actor/', views.addActor, name="addActor"),
    path('add/director/', views.addDirector, name="addDirector"),
    path('add/producer/', views.addProducer, name="addProducer"),
    path('add/movie/', views.addMovie, name="addProducer"),
    path('edit/movie/<id>', views.editMovie, name="editProducer"),

]
