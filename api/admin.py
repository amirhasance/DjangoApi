from django.contrib import admin
from .models import  Movie , Rating


admin.site.register(Movie)
admin.site.register(Rating)
from django.contrib.auth.models import User
# admin.site.register(User)

# Register your models here.
