from .models import Movie

def recent_movies(request):
    movies_ordered_by_date  = Movie.objects.all().order_by('-date')
    if movies_ordered_by_date:
        recent_movies = movies_ordered_by_date[0:9]
    else: 
        recent_movies = None
    return {"recent_movies": recent_movies}


def hot_movies(request):
    movies_ordered_by_views  = Movie.objects.all().order_by('-views')
    if movies_ordered_by_views:
        hot_movies = movies_ordered_by_views[0:9]
    else: 
        hot_movies = None
    return {"hot_movies": hot_movies}


def highlight_movie(request):
    movies_ordered_by_views  = Movie.objects.all().order_by('-views')
    if movies_ordered_by_views:
        highlight_movie = movies_ordered_by_views[0]
    else: 
        highlight_movie = None
    return {"highlight_movie": highlight_movie}