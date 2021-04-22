from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from app.models import *
from app.forms import *


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

def register_user(request):
    if request.method == 'POST':
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            
            new_user.refresh_from_db()
            print(register_form.cleaned_data['favorite_genres'])
            new_user.profile.favorite_genres.set(register_form.cleaned_data['favorite_genres'])
            new_user.profile.email = register_form.cleaned_data['email']

            new_user.save()
            messages.success(request, "Registration successful." )
            return redirect('home')
        messages.error(request, register_form.errors.as_data())
    
    register_form = SignUpForm()
    return render(request, "register.html", {"form":register_form})

def login_user(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"User {username} successfully logged in!")
                return redirect('ListMovies')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        login_form = AuthenticationForm()
        return render(request, "login.html", {"form": login_form})

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
