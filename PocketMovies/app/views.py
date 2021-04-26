from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import *
from app.forms import *

@login_required()
def list_movies(request):
    if 'genre' in request.POST:
        genre = request.POST['genre']
        if genre:
            genre_object = Genre.objects.get(name=genre)
            movies = Movie.objects.filter(genre=genre_object)
    else:
        movies = Movie.objects.all()
    tparams = {'movie_list': movies, 'genre_list': Genre.objects.all()}
    return render(request, 'ListMovies.html', tparams)


@login_required()
def list_actors(request):
    # return render(request, 'ListActors.html', {'actor_list': Actor.objects.all()})
    return render(request, 'ListActors.html')

@login_required()
def list_directors(request):
    # return render(request, 'ListDirectors.html', {'director_list': Director.objects.all()})
    return render(request, 'ListDirectors.html')

@login_required()
def list_producers(request):
    # return render(request, 'ListProducers.html', {'producer_list': Producer.objects.all()})
    return render(request, 'ListProducers.html')

def register_user(request):
    if request.method == 'POST':
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            new_user.refresh_from_db()

            new_user.profile.user.first_name = register_form.cleaned_data['fname']
            new_user.profile.user.last_name = register_form.cleaned_data['lname']
            new_user.profile.user.email = register_form.cleaned_data['email']
            new_user.profile.favorite_genres.set(register_form.cleaned_data['favorite_genres'])

            new_user.save()
            messages.success(request, "Registration successful." )
            return redirect('home')
        messages.error(request, register_form.errors.as_data())
    
    register_form = SignUpForm()
    return render(request, "register.html", {"form":register_form})

def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"User {username} successfully logged in!")
                request.session['username'] = username
                return redirect('ListMovies')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})

def logout_user(request):
    logout(request)
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('home')

    

def home(request):
    return render(request, "layout.html")

@login_required()
def infoProducer(request, id):
    try:
        producer = Producer.objects.get(id=id)
        return render(request, "infoView.html", {"producer": producer})
    except:
        producer = None
        return render(request, "infoView.html")

@login_required()
def infoActor(request, id):
    try:
        actor = Actor.objects.get(id=id)
        return render(request, "infoView.html", {"person": actor})
    except:
        actor = None
        return render(request, "infoView.html")


def infoDirector(request, id):
    try:
        director = Director.objects.get(id=id)
        return render(request, "infoView.html", {"person": director})
    except:
        director = None
        return render(request, "infoView.html")


def infoMovie(request, id):
    try:
        movie = Movie.objects.get(id=id)
        return render(request, "infoView.html", {"movie": movie})
    except Exception as e:
        movie = None
        print(e)
        return render(request, "infoView.html")


def searchMovie(request):
    title = request.GET["title"]
    movie = Movie.objects.filter(title__icontains=title)
    tparams = {'movie_list': movie, 'genre_list': Genre.objects.all()}
    return render(request, 'ListMovies.html', tparams)
