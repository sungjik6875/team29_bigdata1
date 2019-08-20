from .models import Profile, Movie
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    movies = serializers.SerializerMethodField('get_movies')
    # is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'gender', 'age', 'occupation', 'movies')

    def get_username(self, obj):
        return obj.user.username

    def get_movies(self, obj):
        ratings = obj.user.rating_set.all()
        movies = []
        for rating in ratings:
            movies.append(rating.movie.title)
        return movies

    # def get_is_staff(self, obj):
    #     return obj.user.is_staff


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField() 
    view_cnt = serializers.SerializerMethodField('get_views')
    average_rating = serializers.SerializerMethodField('get_average_rating')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'view_cnt', 'average_rating')

    def get_views(self, obj):
        view_cnt = obj.rating_set.all().count() 
        return view_cnt

    def get_average_rating(self, obj):
        total = 0
        view_cnt = obj.rating_set.all().count()
        for rating in obj.rating_set.all():
            total += rating.rating
        
        if view_cnt > 0:
            average_rating = round(total/view_cnt, 3)
        else:
            average_rating = 0
            
        return average_rating 