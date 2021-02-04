from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
	text = models.CharField(max_length=200)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class Place(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=400)
	address = models.CharField(max_length=300, null=True)
	googleAddress = models.CharField(max_length=300, null=True)
	lat = models.FloatField(null=True)
	lng = models.FloatField(null=True)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	comments = models.ManyToManyField(Comment, blank=True, null=True)
	images = models.FileField(null=True)

class Image(models.Model):
	place = models.ForeignKey(Place, default=None, on_delete=models.PROTECT)
	image = models.ImageField(upload_to='images', blank=True, null=True)