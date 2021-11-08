from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Movie(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    publication_date = models.DateTimeField('Date Published')

class Category(models.Model):
    def __str__(self):
        return self.category
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    category = CharField(max_length=200)

class Cast(models.Model):
    def __str__(self):
        return self.actor_actress
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_actress = models.CharField(max_length=200)

