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

    # rating
    url('ratings/$', rating_views.ratings, name="ratings"),
]
