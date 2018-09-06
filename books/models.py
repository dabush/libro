from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Theme(models.Model):
	theme_name = models.CharField(max_length=50)

	def __str__(self):
		return self.theme_name

	class Meta:
		ordering = ('theme_name',)

class Genre(models.Model):
	genre_name = models.CharField(max_length=50)

	def __str__(self):
		return self.genre_name

	class Meta:
		ordering = ('genre_name',)

class Form(models.Model):
	form_name = models.CharField(max_length=50)

	def __str__(self):
		return self.form_name

	class Meta:
		ordering = ('form_name',)

class Period(models.Model):
	period_name = models.CharField(max_length=50)

	def __str__(self):
		return self.period_name

	class Meta:
		ordering = ('period_name',)

class Setting(models.Model):
	setting_name = models.CharField(max_length=100)

	def __str__(self):
		return self.setting_name

	class Meta:
		ordering = ('setting_name',)

class Book(models.Model):
	book_title = models.CharField(max_length=200)
	book_subtitle = models.CharField(max_length=200, blank=True)
	pub_date = models.DateField(auto_now=False)
	pub_year = models.IntegerField()
	publisher = models.CharField(max_length=100)
	author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name="book_to_author")
	cover_image = models.ImageField(null=True, blank=False, upload_to='book_images')
	slug = models.SlugField(max_length=30)
	first_lines = models.TextField(blank=True)
	themes = models.ManyToManyField(Theme, blank=True)
	settings = models.ManyToManyField(Setting, blank=True)
	genres = models.ManyToManyField(Genre, blank=True)
	forms = models.ManyToManyField(Form, blank=True)
	periods = models.ManyToManyField(Period, blank=True)
	book_desc = models.TextField()
	book_country = CountryField()
	book_featured = models.BooleanField()
	lists = models.ManyToManyField('BookList', through='ListEntry', related_name='book_lists')

	def get_absolute_url(self):
		return reverse('books:book_detail', kwargs={'slug': self.slug, 'book_id': self.id})

	def __str__(self):
		return self.book_title

	class Meta:
		ordering = ('book_title',)

class RatingManager(models.Manager):

	def get_rating_or_unsaved_blank_rating(self, book, user):
		try:
			return Rating.objects.get(book=book, user=user)
		except Rating.DoesNotExist:
			return Rating(book=book, user=user)

class Rating(models.Model):
	RATING_CHOICES = (
		(1, '1',),
		(2, '2',),
		(3, '3',),
		(4, '4',),
		(5, '5',),
		(6, '6',),
		(7, '7',),
		(8, '8',),
		(9, '9',),
		(10, '10',),
	)
	value = models.SmallIntegerField(choices=RATING_CHOICES)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	rated_on = models.DateTimeField(auto_now=True)

	objects = RatingManager()
	
	def __str__(self):
		return '%s %s' % (self.book, self.user)

	class Meta:
	 	unique_together = ('user', 'book')

class BookList(models.Model):
	awards = 'Awards'
	editorial = 'Editorial'
	LIST_KINDS = (
		(awards, 'Awards',),
		(editorial, 'Editorial',),
	)
	kind = models.CharField(max_length=20, choices=LIST_KINDS)
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=50)

	def get_absolute_url(self):
		return reverse('books:generic_list', kwargs={'kind': self.kind, 'slug': self.slug, 'booklist_id': self.id})

	def __str__(self):
		return self.name

class ListEntry(models.Model):
	book_list = models.ForeignKey(BookList, related_name='in_list', on_delete=models.CASCADE)
	book = models.ForeignKey(Book, related_name='in_list', on_delete=models.CASCADE)

	def __str__(self):
		return '%s in list %s' % (self.book, self.book_list)