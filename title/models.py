from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.id} {self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.id} {self.name}'


class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(blank=True,)
    description = models.TextField(null=True, blank=True,)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True,
                              blank=True,
                              related_name='genre_titles')
    category = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True,
                                 blank=True,
                                 related_name='category_titles')

    def __str__(self):
        return self.name
