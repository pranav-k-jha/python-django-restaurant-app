from rest_framework import serializers
from meals.models import Meals
from users.models import Profile


class MealsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meals
        fields = '__all__'


class ProfilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
