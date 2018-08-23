from django.db import models
from django_countries.fields import CountryField

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField(auto_now=False)
	country = CountryField()
	date_added = models.DateField(auto_now_add=True)
	author_image = models.ImageField(null=True, blank=True, upload_to='author_images')
	slug = models.SlugField(max_length=30)
	def __str__(self):
		return self.first_name + ' ' + self.last_name 
	