from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating, Profile
from django.contrib.auth.models import User

from api.serializers import MovieSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE'])
def movies(request):

    if request.method == 'GET':
        # Search Movies By Title
        if request.GET.get('key') == 'title':
            id = request.GET.get('id', request.GET.get('movie_id', None))
            title = request.GET.get('title', None)
            movies = Movie.objects.all()

            if id:
                movies = movies.filter(pk=id)
            if title:
                movies = movies.filter(title__icontains=title)

        # Search Movies By Genres
        else: 
            genre = request.GET.get('genre', 'All')
            if genre != 'All': 
                movies = Movie.objects.all().filter(genres__icontains=genre)
            else:
                movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        movies = request.data.get('movies', None)
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)

            if not (id and title and genres):
                continue
            if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
                continue

            Movie(id=id, title=title, genres='|'.join(genres)).save()

        return Response(status=status.HTTP_200_OK)


    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)




@api_view(['GET'])
def get_users_watched_movie(request):
    
    if request.method == 'GET':
        movie_id = request.GET.get('movieId', None)
        movie = Movie.objects.get(pk=movie_id)
        serializer = MovieSerializer(movie, many=False)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)