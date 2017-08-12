# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Film
from .models import Actor
from .models import Genre

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Genre)