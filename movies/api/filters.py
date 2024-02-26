import django_filters

from movies.models import Movie


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['exact', 'gte', 'lte'],
            'director__name': ['icontains'],
            'actors__name': ['icontains'],
        }
