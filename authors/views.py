from django.shortcuts import get_object_or_404, render

from .models import Author


def index(request):
    latest_author_list = Author.objects.order_by('-date_added')[:5]
    context = {'latest_author_list': latest_author_list}
    return render(request, 'authors/index.html', context)

def detail(request, author_id):
	author = get_object_or_404(Author, pk=author_id)
	return render(request, 'authors/detail.html', {'author': author})