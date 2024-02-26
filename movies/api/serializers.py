from rest_framework import serializers

from movies.models import Director, Actor, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors_list = ActorSerializer(source='actors', many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'director', 'actors_list']
