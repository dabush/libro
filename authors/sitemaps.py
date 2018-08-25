from django.contrib.sitemaps import Sitemap 
from .models import Author
from books.models import Book

class AuthorSiteMap(Sitemap):
	changefreq = 'never'
	priority = 0.9

	def items(self):
		return Author.objects.all()

class BookSiteMap(Sitemap):
	changefreq = 'never'
	priority = 0.9

	def items(self):
		return Book.objects.all()