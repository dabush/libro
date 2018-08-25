from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse

class School(models.Model):
	school_name = models.CharField(max_length=50)

	def __str__(self):
		return self.school_name

	class Meta:
		ordering = ('school_name',)

class Region(models.Model):
	region_name = models.CharField(max_length=100)

	def __str__(self):
		return self.region_name

	class Meta:
		ordering = ('region_name',)


class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth_year = models.IntegerField()
	bio = models.TextField()
	country = CountryField()
	schools = models.ManyToManyField(School, blank=True)
	regions = models.ManyToManyField(Region, blank=True)
	date_added = models.DateField(auto_now_add=True)
	author_image = models.ImageField(null=True, blank=True, upload_to='author_images')
	slug = models.SlugField(max_length=30)
	featured_author = models.BooleanField()

	def get_absolute_url(self):
		return reverse('authors:detail', kwargs={'slug': self.slug, 'author_id': self.id})

	def __str__(self):
		return self.first_name + ' ' + self.last_name