from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import Book
from authors.models import Author


class BookPage(TemplateView):
	template_name="books/index.html"
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['books'] = Book.objects.all()
		context['featuredbooks'] = Book.objects.filter(book_featured=True)
		return context

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/index.html', context)

def detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, 'books/detail.html', {'book': book})


class BookDetailPage(TemplateView):
	template_name="books/detail.html"
	def get_context_data(self, **kwargs):
		book = Book.objects.get(pk=self.kwargs['book_id'])
		context = super().get_context_data(**kwargs)
		context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
		context['author_books'] = Book.objects.all().filter(author=book.author).exclude(id=book.id)
		return context

class BrowseAllBooksPage(TemplateView):
	template_name="books/browse.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['books'] = Book.objects.all().order_by('book_title')
		return context