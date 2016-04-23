from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Author(models.Model):
	author_name = models.CharField(max_length=200)
	author_image = models.ImageField(upload_to='team', null=True, blank=True)

	def __str__(self):
		return self.author_name



class Category(models.Model):
	category_name = models.CharField(max_length=200)

	def __str__(self):
		return self.category_name



class Post(models.Model):
	title = models.CharField(max_length=200)
	article = models.TextField()
	pub_date = models.DateField('date published', null=True)
	image = models.ImageField(upload_to='post', null=True, blank=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title



