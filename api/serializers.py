from rest_framework import serializers;
from .models import  Movie , Rating
from django.contrib.auth.models import User
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id' , 'title' , 'description' , 'no_of_rating' , 'avg_rating']

class RatinSerializer (serializers.ModelSerializer):
    class Meta :
        model = Rating
        fields = [ 'id' ,'stars'  , 'user' , 'movie']

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'username' , 'password')
        extra_kwargs = {'password' : {'write_only':False , 'required':True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
     

