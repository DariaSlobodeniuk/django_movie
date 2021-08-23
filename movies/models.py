from datetime import date

from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor and Director"
        verbose_name_plural = "Actors and Directors"


class Ganre(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ganre"
        verbose_name_plural = "Ganres"


class Movie(models.Model):
    title = models.CharField("Title", max_length=160)
    tagline = models.CharField("Tagline", max_length=100, default="")
    description = models.TextField("Description")
    poster = models.ImageField("poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Date of primier", default=2019)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actor")
    genres = models.ManyToManyField(Ganre, verbose_name="genres")
    word_primier = models.DateField("Word primier", default=date.today)
    budget = models.PositiveSmallIntegerField("Budget", default=0, help_text="summ in dollars")
    feeds_in_usa = models.PositiveIntegerField("Feeds in usa", max_length=100, help_text="summ in dollars")
    feeds_in_world = models.PositiveIntegerField("Feeds in world", max_length=100, help_text="summ in dollars")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField("Url", max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shoots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie`s Shoot"
        verbose_name_plural = "Movie`s Shoots"


class RaitingStar(models.Model):
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Raiting`s Star"
        verbose_name_plural = "Raiting`s Stars"


class Raiting(models.Model):
    ip = models.CharField("IP adress", max_length=15)
    star = models.ForeignKey(RaitingStar, verbose_name="Star", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")

    def __str__(self):
        return f"{self.star}-{self.movie}"

    class Meta:
        verbose_name = "Raiting"
        verbose_name_plural = "Raitings"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name",max_length=100)
    text = models.TextField("Messege",max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Parent",on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"