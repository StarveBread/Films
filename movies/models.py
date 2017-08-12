# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Film(models.Model):
	title = models.CharField(max_length=150)
	year = models.DateTimeField()
	actor = models.ManyToManyField("Actor",related_name="Film")
	genre = models.ManyToManyField("Genre",related_name="Film")
	
	
	def __str__(self):
		return self.title
		#return "{} actor {}".format(self.title,self.list_actor())

	#def list_actor(self):
	#	return ",".join([actor.first_name for actor in self.actor.all()])

	def save(self, *args,**kwargs):
		super(Film,self).save(*args,**kwargs)
		
		
class Actor(models.Model):
	first_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	
	def __str__(self):
		return self.last_name
		
	def save(self, *args,**kwargs):
		super(Actor,self).save(*args,**kwargs)
		
		
		
class Genre(models.Model):
	type_name = models.CharField(max_length=150)
	description = models.TextField(max_length=500)
	
	def __str__(self):
		return self.type_name
		