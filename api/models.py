from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator , MaxValueValidator
class Movie(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=360)
    def no_of_rating(self):
        return Rating.objects.filter(movie=self).count()

    def avg_rating (self):
        sum = 0;
        for x in Rating.objects.filter(movie=self):
            sum += x.stars
        if self.no_of_rating() != 0:
            return  sum/self.no_of_rating()
        else :
            return 0


    def __str__(self):
        return f'title : {self.title}'

class Rating (models.Model):
    movie = models.ForeignKey(Movie , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])

    def __str__(self):
        return f'movie : {self.movie.title} ; star : {self.stars}  ; user : {self.user}'


    class Meta:
        unique_together = (('user' , 'movie') ,)
        index_together = (('user', 'movie') , )
# Create your models here.
