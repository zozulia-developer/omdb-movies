from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    year = models.PositiveIntegerField(
        default=2024,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(9999)
        ]
    )
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title
