import requests
from django.conf import settings
from django.core.management import BaseCommand

from movies.models import Actor, Director, Movie


class Command(BaseCommand):
    help = 'Fetches movie from the API and saves them to the database'

    def add_arguments(self, parser):
        parser.add_argument('search_query', nargs='?', default='star wars', help='Search query string for movies')

    def handle(self, *args, **options):
        api_key = settings.OMDB_API_KEY
        search_query = options['search_query']
        url = f'http://www.omdbapi.com/?apikey={api_key}&t={search_query}&type=movie'
        response = requests.get(url)
        response_movie = response.json()

        director_name = response_movie['Director']
        director, _ = Director.objects.get_or_create(name=director_name)

        actors = [
            Actor.objects.get_or_create(name=actor_name.strip())[0]
            for actor_name in response_movie['Actors'].split(',')
        ]

        movie, created = Movie.objects.get_or_create(
            title=response_movie['Title'],
            year=int(response_movie['Year']),
            director=director
        )
        if created:
            movie.actors.add(*actors)
            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved movie'))
        else:
            self.stdout.write(self.style.WARNING('Movie already exists'))
