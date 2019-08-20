from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile

from django.contrib.auth.models import User
from api.models import Profile, Rating, Movie
from api.serializers import ProfileSerializer

from django.shortcuts import get_object_or_404


@api_view(['POST'])
def signup_many(request):

    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)

        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_user_info(request):
    print(request.GET.get("userId"))
    user_id = request.GET.get("userId")
    print("django", user_id)
    user = User.objects.get(pk=user_id)
    user_info = Profile.objects.get(user=user)

    serializer = ProfileSerializer(user_info, many=False)
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    
    

