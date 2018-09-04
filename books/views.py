from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, RedirectView, FormView
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import simplejson as json

from .models import Book, Rating
from .forms import RatingForm
from .mixins import AjaxFormMixin
from authors.models import Author
from common.decorators import ajax_required


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


@ajax_required
@login_required
@require_POST
def book_like(request, slug, book_id):
	book_id = request.POST.get('id')
	slug = request.POST.get('slug')
	action = request.POST.get('action')
	if book_id and action:
		try:
			book = Book.objects.get(id=book_id)
			if action == 'like':
				book.likes.add(request.user)
			else:
				book.likes.remove(request.user)
			return JsonResponse({'status':'ok'})
		except:
			pass
	return JsonResponse({'status':'ko'})

@login_required
def book_list(request):
	books = Book.objects.all()
	#set to 999 to deal with bug that causes repeat
	paginator = Paginator(books, 999)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer deliver the first page
		pages = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			#if the request is ajax and the page is out of range return an empty page
			return HttpResponse('')
		#if page is out of range deliver the last page of results
		books = paginator.page(paginator.num_pages)
	if request.is_ajax():
		return render(request, 'books/list_ajax.html', {'section': 'books', 'books': books})
	return render(request, 'books/list.html', {'section': 'books', 'books': books})


class RatingFormView(AjaxFormMixin, FormView):
	form_class = RatingForm
	template_name  = 'books/_rate.html'
	success_url = '/'