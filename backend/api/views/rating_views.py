from rest_framework import status
from rest_framework.decorators import api_view


from api.models import Movie, Rating
from django.contrib.auth.models import User

from rest_framework.response import Response



@api_view(['GET','POST', 'DELETE'])
def ratings(request):

  # create Ratings
  if request.method == 'POST':
      ratings = request.data.get('ratings', None)
      for rating_data in ratings:
          user_id = rating_data.get('user_id', None)
          movie_id = rating_data.get('movie_id', None)


          user = User.objects.get(pk=user_id)
          movie = Movie.objects.get(pk=movie_id)
          
          rating = rating_data.get('rating', None)
          created_at = rating_data.get('timestamp', None)


          Rating(user=user, movie=movie, rating=rating, created_at=created_at).save()

      return Response(status=status.HTTP_200_OK)
    