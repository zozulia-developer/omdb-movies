from rest_framework import serializers

from movies.models import Actor, Director, Movie


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

    def create(self, validated_data):
        director_data = validated_data.pop('director')
        actors_data = validated_data.pop('actors')

        director, _ = Director.objects.get_or_create(**director_data)
        actors = [Actor.objects.get_or_create(**actor_data)[0] for actor_data in actors_data]

        movie = Movie.objects.create(director=director, **validated_data)
        movie.actors.set(actors)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)

        director_data = validated_data.get('director')
        if director_data:
            director, _ = Director.objects.get_or_create(**director_data)
            instance.director = director

        actors_data = validated_data.get('actors')
        if actors_data:
            actors = [Actor.objects.get_or_create(**actor_data)[0] for actor_data in actors_data]
            instance.actors.set(actors)

        instance.save()
        return instance
