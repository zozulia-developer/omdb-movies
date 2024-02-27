from django.urls import path

from .views import AddMovieView, MovieDeleteView, MovieDetailView, MovieListView, MovieUpdateView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('add-movie/', AddMovieView.as_view(), name='add_movie'),
    path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='edit_movie'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='delete_movie'),
]
