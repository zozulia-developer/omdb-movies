from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView, TemplateView

from movies.models import Movie


class HomePageView(TemplateView):
    template_name = 'base.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = context['movies']
        paginator = Paginator(movies, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)
        context['movies'] = movies
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
