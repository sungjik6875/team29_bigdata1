from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


    @property
    def movies(self):
        ratings = self.rating_set.all()
        movies_list = []
        for rating in ratings:
            movies_list.append(rating.movie.title)
        return movies_list


#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)

    users = models.ManyToManyField(User, related_name="movies", blank=True)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')

    @property
    def view_cnt(self):
        return self.rating_set.all().count()

    @property
    def average_rating(self):
        views = self.rating_set.all().count()
        if views == 0:
            return 0

        ratings = self.rating_set.all()
        total = 0
        for rating in ratings:
            total += rating.rating
        return round(total/views, 3)
        
    def __str__(self):
        return self.title


class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return "{} / {} / {}".format(self.user.username, self.movie.title, self.rating)