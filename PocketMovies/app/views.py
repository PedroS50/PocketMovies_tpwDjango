from django.shortcuts import render
from app.models import *


def list_movies(request):
    # return render(request, 'ListMovies.html', {'movie_list': Movie.objects.all()})
    return render(request, 'ListMovies.html')

def list_actors(request):
    # return render(request, 'ListActors.html', {'actor_list': Actor.objects.all()})
    return render(request, 'ListActors.html')

def list_directors(request):
    # return render(request, 'ListDirectors.html', {'director_list': Director.objects.all()})
    return render(request, 'ListDirectors.html')

def list_producers(request):
    # return render(request, 'ListProducers.html', {'producer_list': Producer.objects.all()})
    return render(request, 'ListProducers.html')
