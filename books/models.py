from django.db import models

class Book(models.Model):
	book_title = models.CharField(max_length=200)
	pub_date = models.DateField(auto_now=False)
	publisher = models.CharField(max_length=100)
	author = models.ForeignKey('authors.Author', on_delete=models.CASCADE,)
	cover_image = models.ImageField(null=True, blank=True, upload_to='book_images')
	slug = models.SlugField(max_length=30)
	def __str__(self):
		return self.book_title