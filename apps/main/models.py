from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):

	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Category(models.Model):

	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Notice(models.Model):

	category = models.ForeignKey(Category)
	author = models.ForeignKey(Author)
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	resumen = models.TextField(max_length=300)
	description = models.TextField(max_length=1000)
	image = models.ImageField(upload_to = 'notice')
	created = models.DateTimeField(auto_now_add=True)
	main = models.BooleanField(default = False)
	

	def __unicode__(self):
		return self.title

class Comment(models.Model):

	notice = models.ForeignKey(Notice)
	user = models.ForeignKey(User)
	comment = models.TextField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.user.username