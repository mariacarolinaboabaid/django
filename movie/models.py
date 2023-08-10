from django.db import models
from django.contrib.auth.models import AbstractUser

LIST_CATEGORIES = (
    ("ACTION" , "Action"), 
    ("COMEDY", "Comedy"),
    ("DRAMA", "Drama"),
    ("ROMANCE", "Romance"),
    ("DOCUMENTARY", "Documentary"),
    ("SUSPENSE", "Suspense"),
    ("HORROR", "Horror"),
    ("SCIENCE_FICTION", "Science Fiction")
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    filmCover = models.ImageField(upload_to="covers", default="covers/default_cover.jpg")
    image = models.ImageField(upload_to="images_movies")
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=20, choices=LIST_CATEGORIES)
    views = models.IntegerField(default=0)
    date = models.DateTimeField()
    
    # String representation 
    def __str__(self):
        return self.title
    
    
class Trailer(models.Model):
    movie = models.ForeignKey("Movie", related_name="trailers", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    
    # String representation 
    def __str__(self):
        return self.movie.title + " - " + self.title


class User(AbstractUser):
    seen_movies = models.ManyToManyField("Movie")
    

    
    
