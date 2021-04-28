from django import template
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import *
from app.forms import *


@login_required()
def list_movies(request, movie):
    profile = Profile.objects.get(user=User.objects.get(username=request.session['username']))
    genre = ''
    if movie == 'all':
        movies = Movie.objects.all()
    elif movie == 'my_favorite_movies':
        movies = profile.favorite_movies.all()
    elif movie == 'my_want_to_watch':
        movies = profile.want_to_watch.all()
    elif movie == 'my_watched_movies':
        movies = profile.movies_watched.all()

    if 'genre' in request.POST:
        genre = request.POST['genre']
        if genre:
            genre_object = Genre.objects.get(name=genre)
            movies = movies.filter(genre=genre_object)

    if 'title' in request.GET:
        search_term = request.GET['title']
        movies = movies.filter(title__icontains=search_term)

    if 'add_movie_watched' in request.POST:
        movie_id = request.POST['add_movie_watched']
        if movie_id:
            movie = movies.get(id=movie_id)
            profile.movies_watched.add(movie)
    if 'remove_movie_watched' in request.POST:
        movie_id = request.POST['remove_movie_watched']
        if movie_id:
            movie = movies.get(id=movie_id)
            profile.movies_watched.remove(movie)
    if 'add_favorite_movies' in request.POST:
        movie_id = request.POST['add_favorite_movies']
        if movie_id:
            movie = movies.get(id=movie_id)
            profile.favorite_movies.add(movie)
    if 'remove_favorite_movies' in request.POST:
        movie_id = request.POST['remove_favorite_movies']
        if movie_id:
            movie = movies.get(id=movie_id)
            profile.favorite_movies.remove(movie)
    if 'add_want_to_watch' in request.POST:
        movie_id = request.POST['add_want_to_watch']
        if movie_id:
            movie = movies.get(id=movie_id)
            profile.want_to_watch.add(movie)
    if 'remove_want_to_watch' in request.POST:
        movie_id = request.POST['remove_want_to_watch']
        if movie_id:
            movie = movies.get(id=movie_id)
            profile.want_to_watch.remove(movie)

    tparams = {'movie_list': movies, 'genre_list': Genre.objects.all(), 'selected_genre': genre, 'profile': profile}
    return render(request, 'ListMovies.html', tparams)
    # return render(request, 'ListMovies.html')


@login_required()
def list_people(request, person):
    if person == 'actors':
        people = Actor.objects.all()
    elif person == 'producers':
        people = Producer.objects.all()
    elif person == 'directors':
        people = Director.objects.all()
    return render(request, 'ListActors.html', {'person_list': people, 'person_role': person.upper()})


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

            group = Group.objects.get(name="client")
            new_user.groups.add(group)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, register_form.errors.as_data())

    register_form = SignUpForm()
    return render(request, "register.html", {"form": register_form})


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
                return render(request, "login.html", {"form": login_form})
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html", {"form": login_form})
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
    print(request.user.groups.all())
    return render(request, "layout.html", {"user": request.user})


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
    profile = Profile.objects.get(user=User.objects.get(username=request.session['username']))
    try:
        movie = Movie.objects.get(id=id)
        return render(request, "infoView.html", {"movie": movie, "profile": profile})
    except Exception as e:
        movie = None
        print(e)
        return render(request, "infoView.html")


def searchMovie(request):
    title = request.GET["title"]
    movie = Movie.objects.filter(title__icontains=title)
    tparams = {'movie_list': movie, 'genre_list': Genre.objects.all()}
    return redirect('/movies/', tparams)


def addActor(request):
    if request.POST:
        form = AddActorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            birthdate = form.cleaned_data["birthdate"]
            years_active = form.cleaned_data["years_active"]
            nationality = form.cleaned_data["nationality"]
            twitter = form.cleaned_data["twitterAccount"]
            instagram = form.cleaned_data["instagramAccount"]
            imageField = form.cleaned_data["imageField"]
            Actor.objects.create(name=name, birthdate=birthdate, imageField=imageField, years_active=years_active,
                                 nationality=nationality, twitterAccount=twitter, instagramAccount=instagram)
            return redirect('/actors')
        else:
            print(form.errors)
            return redirect('/actors')
    return render(request, "addActor.html", {"form": AddActorForm(), "url": "actor"})


def addDirector(request):
    if request.POST:
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            birthdate = form.cleaned_data["birthdate"]
            nationality = form.cleaned_data["nationality"]
            twitter = form.cleaned_data["twitterAccount"]
            instagram = form.cleaned_data["instagramAccount"]
            website = form.cleaned_data["website"]
            imageField = form.cleaned_data["imageField"]
            Director.objects.create(name=name, birthdate=birthdate,
                                    nationality=nationality, website=website, imageField=imageField,
                                    twitterAccount=twitter,
                                    instagramAccount=instagram)
            return redirect('/directors')
        else:
            return redirect('/actors')
    return render(request, "addActor.html", {"form": AddDirectorForm(), "url": "director"})

def addProducer(request):
    if request.POST:
        form = AddProducerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            country = form.cleaned_data["country"]
            city = form.cleaned_data["city"]
            twitter = form.cleaned_data["twitterAccount"]
            instagram = form.cleaned_data["instagramAccount"]
            website = form.cleaned_data["website"]
            imageField = form.cleaned_data["imageField"]
            Producer.objects.create(name=name, country=country,
                                    city=city, website=website, imageField=imageField,
                                    twitterAccount=twitter,
                                    instagramAccount=instagram)
            return redirect('/producers')
        else:
            return redirect('/producers')
    return render(request, "addActor.html", {"form": AddProducerForm(), "url": "producer"})
