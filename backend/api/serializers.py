from .models import Profile, Movie
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    movies = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    
    # is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'gender', 'age', 'occupation', 'movies')

    def get_username(self, obj):
        return obj.user.username

    # def get_is_staff(self, obj):
    #     return obj.user.is_staff


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField() 
    view_cnt = serializers.ReadOnlyField() 
    average_rating = serializers.ReadOnlyField() 

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'view_cnt', 'average_rating')

