from rest_framework import serializers;
from .models import  Movie , Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id' , 'title' , 'description' , 'no_of_rating' , 'avg_rating']

class RatinSerializer (serializers.ModelSerializer):
    class Meta :
        model = Rating
        fields = [ 'id' ,'stars'  , 'user' , 'movie']

