from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, RedirectView, FormView
from django.http import JsonResponse, HttpResponse
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

import simplejson as json

from .models import Book, Rating, BookList, ListEntry
from .forms import RatingForm
from account.models import UserListEntry
from account.forms import UserEntryAddForm
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
		userlist_entry_form = UserEntryAddForm
		listentry_form_url = ''
		rating_form_url = ''
		if self.request.user.is_authenticated:
			listentry_form_url = reverse('books:user_list_add', kwargs={'slug': self.kwargs['slug'], 'book_id': self.kwargs['book_id']})
			rating = Rating.objects.get_rating_or_unsaved_blank_rating(book=book, user=self.request.user)
			userlist_entry_form = UserEntryAddForm(self.request.user)
			if rating.id:
				rating_form_url = reverse('books:update_rating', kwargs={'slug': rating.book.slug, 'book_id': rating.book.id, 'pk': rating.id})
				context['rating'] = rating
			else:
				rating_form_url = reverse('books:rate', kwargs={'slug': rating.book.slug, 'book_id': rating.book.id})
		context['rate_form'] = RatingForm
		context['rating_form_url'] = rating_form_url
		context['average_rating'] = Rating.objects.filter(book=book).aggregate(Avg('value'))
		context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
		context['author_books'] = Book.objects.all().filter(author=book.author).exclude(id=book.id)
		context['listentry_form_url'] = listentry_form_url
		context['userlist_entry_form'] = userlist_entry_form
		return context

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
	def get_initial(self):
		initial = super().get_initial()
		initial['user'] = self.request.user.id
		initial['book'] = self.kwargs['book_id']
		return initial

	form_class = RatingForm
	template_name  = 'books/_rate.html'
	success_url = '/'

class UpdateRatingFormView(UserPassesTestMixin, AjaxFormMixin, UpdateView):
	form_class = RatingForm
	template_name = 'books/_rate.html'
	model = Rating
	success_url = '/'

	def test_func(self):
		self.object = self.get_object()
		return self.request.user == self.object.user

class DeleteRatingView(UserPassesTestMixin, AjaxFormMixin, DeleteView):
	model = Rating
	template_name = 'books/_rating_delete.html'
	success_url = reverse_lazy('accounts:dashboard')

	def test_func(self):
		self.object = self.get_object()
		return self.request.user == self.object.user

class AllLists(TemplateView):
	template_name = 'books/all_lists.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['award_lists'] = BookList.objects.filter(kind='awards')
		context['editorial_lists'] = BookList.objects.filter(kind='editorial')
		return context

class ListsOfKind(TemplateView):
	template_name = 'books/lists_of_kind.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['kind'] = self.kwargs['kind']
		context['lists_of_kind'] = BookList.objects.filter(kind=self.kwargs['kind'])
		return context

class GenericList(TemplateView):
	template_name = 'books/generic_list.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		book_list = BookList.objects.get(slug=self.kwargs['slug'])
		context['list_entries'] = ListEntry.objects.filter(book_list=book_list).order_by('-year')
		context['kind'] = self.kwargs['kind']
		context['list'] = BookList.objects.get(slug=self.kwargs['slug'])
		return context

class UserListEntryView(LoginRequiredMixin, AjaxFormMixin, CreateView):
	def get_form_kwargs(self):
		kwargs = super(UserListEntryView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def get_initial(self):
		initial = super().get_initial()
		initial['user'] = self.request.user.id
		initial['book'] = self.kwargs['book_id']
		return initial

	model = UserListEntry
	form_class = UserEntryAddForm
	template_name = 'books/_list_add.html'
	success_url = '/'