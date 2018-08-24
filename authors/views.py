from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView

from .models import Author
from books.models import Book



class AuthorPage(TemplateView):
	template_name="authors/index.html"
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['authors'] = Author.objects.all()
		context['featuredauthors'] = Author.objects.filter(featured_author=True)
		return context

def index(request):
    latest_author_list = Author.objects.order_by('-date_added')[:5]
    context = {'latest_author_list': latest_author_list}
    return render(request, 'authors/index.html', context)

class AuthorDetailPage(TemplateView):
	template_name="authors/detail.html"
	def get_context_data(self, **kwargs):
		author = Author.objects.get(pk=self.kwargs['author_id'])
		context = super().get_context_data(**kwargs)
		context['author'] = Author.objects.get(pk=self.kwargs['author_id'])
		context['books'] = Book.objects.filter(author=author)
		return context

class BrowseAllAuthorsPage(ListView):
	queryset = Author.objects.all()
	paginate_by = 1
	template_name="authors/browse.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['authors'] = Author.objects.all().order_by('last_name')
		context['books'] = Book.objects.all()
		return context
