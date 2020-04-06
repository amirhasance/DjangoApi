from django.urls import path
from rest_framework import  routers
from django.conf.urls import include
from .views import  MovieViewSet ,RatingViewSet , myFunction

router = routers.DefaultRouter()
router.register('movies' , MovieViewSet )
router.register('ratings' , RatingViewSet )
urlpatterns = [
    path('myFunction' , myFunction),
    path('', include(router.urls)),

]
