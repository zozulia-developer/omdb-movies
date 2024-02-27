from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from movies.forms import AddMovieForm, EditMovieForm
from movies.models import Movie


class HomePageView(TemplateView):
    template_name = 'base.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'
    paginate_by = 25

    def get_queryset(self):
        return Movie.objects.order_by('title')

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


class AddMovieView(CreateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'movies/add_movie.html'
    success_url = reverse_lazy('home')


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = EditMovieForm
    template_name = 'movies/edit_movie.html'
    success_url = reverse_lazy('home')


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('home')
