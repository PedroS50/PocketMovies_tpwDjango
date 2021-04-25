from django.shortcuts import render
from app.models import *


def list_movies(request):
    genre = ''
    movies = Movie.objects.all()

    if 'genre' in request.POST:
        genre = request.POST['genre']
        if genre:
            genre_object = Genre.objects.get(name=genre)
            movies = Movie.objects.filter(genre=genre_object)

    tparams = {'movie_list': movies, 'genre_list': Genre.objects.all(), 'selected_genre': genre}
    return render(request, 'ListMovies.html', tparams)
    #return render(request, 'ListMovies.html')


def list_actors(request):
    # return render(request, 'ListActors.html', {'actor_list': Actor.objects.all()})
    return render(request, 'ListActors.html')


def list_directors(request):
    # return render(request, 'ListDirectors.html', {'director_list': Director.objects.all()})
    return render(request, 'ListDirectors.html')


def list_producers(request):
    # return render(request, 'ListProducers.html', {'producer_list': Producer.objects.all()})
    return render(request, 'ListProducers.html')


def home(request):
    return render(request, "layout.html")


def infoProducer(request, id):
    try:
        producer = Producer.objects.get(id=id)
        return render(request, "infoView.html", {"producer": producer})
    except:
        producer = None
        return render(request, "infoView.html")


def infoActor(request, id):
    try:
        actor = Actor.objects.get(id=id)
        return render(request, "infoView.html", {"person": actor})
    except:
        producer = None
        return render(request, "infoView.html")
