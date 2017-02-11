#from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import random


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		self.user.username

class ClothingType(models.Model):
	name = models.CharField(max_length=128, unique=True)
	user = models.ForeignKey(User)
	price = models.IntegerField(default=0)
	picture = models.ImageField()
	purchased_at = models.DateTimeField(auto_now=True)
	pos_x = models.IntegerField(random.randint(-10, 15)) #this and next two lines will help give the position of clothing on the 3D plane
	pos_y = models.IntegerField(random.randint(-5, 5))
	pos_z = models.IntegerField(-5)
	size = models.CharField(max_length=128, unique=True)
	color = models.CharField(max_length=128, unique=True)
	season = models.CharField(max_length=128, unique=True)

#class Size(models.Model):
#	name = models.CharField(max_length=128, unique=True)

#class Color(models.Model):
#	name = models.CharField(max_length=128, unique=True)

#class Season(models.Model):
#	name = models.CharField(max_length=128, unique=True)

#class Accessory(models.Model):
#	name = models.CharField(max_length=128, unique=True)
#	user = models.ForeignKey(User)