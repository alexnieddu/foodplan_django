from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return '%s' % self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return '%s' % self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    background_color = models.IntegerField()
    image = models.ImageField()
    ingredients = models.ManyToManyField(Ingredient)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return '%s' % self.name
