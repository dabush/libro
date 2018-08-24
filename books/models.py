from django.db import models
from django_countries.fields import CountryField

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
	author = models.ForeignKey('authors.Author', on_delete=models.CASCADE,)
	cover_image = models.ImageField(null=True, blank=True, upload_to='book_images')
	slug = models.SlugField(max_length=30)
	themes = models.ManyToManyField(Theme, blank=True)
	settings = models.ManyToManyField(Setting, blank=True)
	genres = models.ManyToManyField(Genre, blank=True)
	forms = models.ManyToManyField(Form, blank=True)
	periods = models.ManyToManyField(Period, blank=True)
	book_desc = models.TextField()
	book_country = CountryField()
	book_featured = models.BooleanField()

	def __str__(self):
		return self.book_title

	class Meta:
		ordering = ('book_title',)
