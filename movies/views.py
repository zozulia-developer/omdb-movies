from django.views.generic import ListView, DetailView, TemplateView

from movies.models import Movie


class HomePageView(TemplateView):
    template_name = 'base.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
