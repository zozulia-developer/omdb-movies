from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from movies.api.filters import MovieFilter
from movies.api.serializers import MovieSerializer
from movies.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ['year']
