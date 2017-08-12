# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View


from .models import Film
from .models import Actor
from .models import Genre
# Create your views here.

def list_films(request):
		movies = Film.objects.exclude()
		context = {
		'movies' : movies,
		}
		return render(request,"index.html",context)
		
		
class actors_list(View):
	def get(self,request):
		actors = Actor.objects.all()
		context = {
		'actors' : actors,
		}
		return render(request,"actors.html",context)
		
		
class genres_list(View):
	def get(self,request):
		genres = Genre.objects.all()
		context = {
		'genres' : genres,
		}
		return render(request,"genres.html",context)