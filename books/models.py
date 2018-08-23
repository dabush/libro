from django.db import models
from django_countries.fields import CountryField

class Book(models.Model):
	book_title = models.CharField(max_length=200)
	book_subtitle = models.CharField(max_length=200, blank=True)
	pub_date = models.DateField(auto_now=False)
	pub_year = models.IntegerField()
	publisher = models.CharField(max_length=100)
	author = models.ForeignKey('authors.Author', on_delete=models.CASCADE,)
	cover_image = models.ImageField(null=True, blank=True, upload_to='book_images')
	slug = models.SlugField(max_length=30)
	book_desc = models.TextField()
	book_country = CountryField()
	book_featured = models.BooleanField()
	def __str__(self):
		return self.book_title