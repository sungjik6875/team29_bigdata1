from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views


urlpatterns = [
    # user
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('auth/user_info/$', auth_views.get_user_info, name="get_user_profile"),

    # movie
    url('movies/$', movie_views.movies, name='movies'),
    url('movie/$', movie_views.get_users_watched_movie, name="get_users_watched_movie"),

    # rating
    url('ratings/', rating_views.ratings, name="ratings"),
]
