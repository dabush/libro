from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse
from django.contrib.auth.models import User

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
	full_name = models.CharField(max_length=100)
	birth_year = models.IntegerField()
	bio = models.TextField()
	country = CountryField()
	schools = models.ManyToManyField(School, blank=True)
	regions = models.ManyToManyField(Region, blank=True)
	date_added = models.DateField(auto_now_add=True)
	author_image = models.ImageField(null=True, blank=True, upload_to='author_images')
	slug = models.SlugField(max_length=30)
	featured_author = models.BooleanField()
	likes = models.ManyToManyField(User, related_name="author_likes", blank=True)
	lists = models.ManyToManyField('AuthorList', through='AuthorListEntry', related_name='author_lists')

	def get_absolute_url(self):
		return reverse('authors:detail', kwargs={'slug': self.slug, 'author_id': self.id})

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class AuthorList(models.Model):
	awards = 'awards'
	editorial = 'editorial'
	LIST_KINDS = (
		(awards, 'awards',),
		(editorial, 'editorial',),
	)
	kind = models.CharField(max_length=20, choices=LIST_KINDS)
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=50)
	list_desc = models.TextField()
	list_image = models.ImageField(null=True, blank=True, upload_to='list_images')

	def get_absolute_url(self):
		return reverse('authors:generic_author_list', kwargs={'kind': self.kind, 'slug': self.slug, 'authorlist_id': self.id})

	def __str__(self):
		return self.name

class AuthorListEntry(models.Model):
	author_list = models.ForeignKey(AuthorList, related_name='in_list', on_delete=models.CASCADE)
	author = models.ForeignKey(Author, related_name='in_list', on_delete=models.CASCADE)
	year = models.IntegerField()

	def __str__(self):
		return '%s in list %s for year%s' % (self.author, self.author_list, self.year)