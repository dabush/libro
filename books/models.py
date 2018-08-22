from django.db import models

class Book(models.Model):
	book_title = models.CharField(max_length=200)
	pub_date = models.DateField(auto_now=False)
	publisher = models.CharField(max_length=100)
	author = models.ForeignKey('authors.Author', on_delete=models.CASCADE,)
	def __str__(self):
		return self.book_title