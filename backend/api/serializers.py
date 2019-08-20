from .models import Profile, Movie
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    movies = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    
    # is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'gender', 'age', 'occupation')

    def __init__(self, *args, **kwargs):
        if kwargs.get('many') == False:
            self.Meta.fields = list(self.Meta.fields)
            self.Meta.fields.append('movies')
        super().__init__(*args, **kwargs)

    def get_username(self, obj):
        return obj.user.username

    # def get_is_staff(self, obj):
    #     return obj.user.is_staff


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField() 
    view_cnt = serializers.ReadOnlyField() 
    average_rating = serializers.ReadOnlyField()
    # users = serializers.ReadOnlyField()


    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'view_cnt', 'average_rating')

    def __init__(self, *args, **kwargs):
        if kwargs.get('many') == False:
            self.Meta.fields = list(self.Meta.fields)
            self.Meta.fields.append('users')
        super().__init__(*args, **kwargs)