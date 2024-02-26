from django.urls import path
from .views import MovieListView, MovieDetailView, HomePageView

urlpatterns = [
    path('', MovieListView.as_view(), name='home'),
    # path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]
