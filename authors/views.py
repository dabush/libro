from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Author
from books.models import Book
from common.decorators import ajax_required


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
		context['same_country'] = Author.objects.all().filter(country=author.country).exclude(id=author.id)
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

@ajax_required
@login_required
@require_POST
def author_like(request, slug, author_id):
	author_id = request.POST.get('id')
	slug = request.POST.get('slug')
	action = request.POST.get('action')
	if author_id and action:
		try:
			author = Author.objects.get(id=author_id)
			if action == 'like':
				author.likes.add(request.user)
			else:
				author.likes.remove(request.user)
			return JsonResponse({'status':'ok'})
		except:
			pass
	return JsonResponse({'status':'ko'})