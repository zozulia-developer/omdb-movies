from django.urls import path

from .views import MovieDetailView, MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]
