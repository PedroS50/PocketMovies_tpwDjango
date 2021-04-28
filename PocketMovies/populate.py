import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PocketMovies.settings')

import django
django.setup()

from app.models import Movie, Genre, Actor, Director, Producer
from dataset import movies, genres, actors, directors, producers

for genre in genres:
	new_genre = Genre(name=genre)
	new_genre.save()

for actor in actors:
	new_actor = Actor(
		name=actor['name'],
		birthdate=actor['birthdate'],
		years_active=actor['years_active'],
		nationality=actor['nationality'],
		imageField=actor['imageField'],
		twitterAccount=actor['twitterAccount'],
		instagramAccount=actor['instagramAccount']
	)
	new_actor.save()

for director in directors:
	new_director = Director(
		name=director['name'],
		birthdate=director['birthdate'],
		website=director['website'],
		imageField=director['imageField'],
		twitterAccount=director['twitterAccount'],
		instagramAccount=director['instagramAccount']
	)
	new_director.save()

for producer in producers:
	new_producer = Producer(
		name=producer['name'],
		city=producer['city'],
		country=producer['country'],
		website=producer['website'],
		imageField=producer['imageField'],
		twitterAccount=producer['twitterAccount'],
		instagramAccount=producer['instagramAccount']
	)
	new_producer.save()
# {'title': '', 'description': '', 'rating': 0, 'director': [''], 'producer': '', 'cast': ['', '', '', ''], 'genre': [''], 'imageField': '',  'published_date': datetime.date(2021, 4, 23)},

for movie in movies:
	new_movie = Movie(
		title=movie['title'],
		description=movie['description'],
		rating=movie['rating'],
		imageField=movie['imageField'],
		published_date=movie['published_date']
	)

	new_movie.save()
	new_movie.refresh_from_db()

	for genre in movie['genre']:
		new_movie.genre.add( Genre.objects.filter(name=genre).first().id )

	for director in movie['director']:
		new_movie.director.set( Director.objects.filter(name=director) )

	new_movie.producer.set( Producer.objects.filter(name=movie['producer']) )

	for actor in movie['cast']:
		new_movie.cast.add( Actor.objects.filter(name=actor).first().id )
	
	new_movie.save()

