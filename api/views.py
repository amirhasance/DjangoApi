from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets , status
from rest_framework.decorators import  action
from .models import  Movie ,Rating
from .serializers import MovieSerializer , RatinSerializer , UserSerializer
from rest_framework.response import  Response
from .models import  User
from rest_framework.parsers import  JSONParser
from django.http import JsonResponse
from rest_framework.authentication import  TokenAuthentication

class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes =  (TokenAuthentication , )


    @action(detail=True , methods=['POST' , 'GET']  )
    def rate_movie(self , request , pk = None):
        #import pdb;
        #pdb.set_trace();
        # print(dir(request.data))
        # print(request.data)
        user = request.user
        print('user ' , user)

        # print(f'username {user.username} , password {user.password} , pk {user.pk}')
        print(f'now here ///////////////// and {request.data}')
        if 'stars' in request.data:

            try :
               rate_obj =  Rating.objects.get(movie=pk , user = user  )
               rate_obj.stars = request.data['stars']
               rate_obj.save()
               serializer = RatinSerializer(rate_obj , many=False)
               return Response({'message' : 'rating is updated ' , 'result' : serializer.data } , status=status.HTTP_200_OK)

            except:
                rate_obj = Rating.objects.create(movie=pk, user = user , stars=request.data['stars'])
                serializer = RatinSerializer(rate_obj , many=False)
                return Response({'message ': 'created rating ' , 'result' : serializer.data } , status=status.HTTP_200_OK)

        else :
            return Response({'message' : 'no star found in request.data' } , status= status.HTTP_404_NOT_FOUND)





class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    authentication_classes = (TokenAuthentication  , )
    serializer_class = RatinSerializer
# Create your views here.
@csrf_exempt
def myFunction (request):
    if request.method == 'GET':
        print("my function is running ")
        serializer = MovieSerializer(Movie.objects.first(), many=False)
        return JsonResponse({'message' : 'its working fine ' , 'result' : serializer.data})
    elif request.method == 'POST':
        data= JSONParser.parse(request)
