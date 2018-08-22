from django.shortcuts import get_object_or_404, render

from .models import Book


def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/index.html', context)

def detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, 'books/detail.html', {'book': book})