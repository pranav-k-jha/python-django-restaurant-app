from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MealsSerializer
from .serializers import ProfilesSerializer
from meals.models import Meals
from users.models import Profile


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/meals'},
        {'GET': '/api/meals/id'},

        {'GET': '/api/profiles'},
        {'GET': '/api/profiles/id'},
        #{'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProfiles(request):
    print('USER:', request.user)
    profiles = Profile.objects.all()
    serializer = ProfilesSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfilesSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getMeals(request):
    meals = Meals.objects.all()
    serializer = MealsSerializer(meals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMeal(request, pk):
    meal = Meals.objects.get(id=pk)
    serializer = MealsSerializer(meal, many=False)
    return Response(serializer.data)
