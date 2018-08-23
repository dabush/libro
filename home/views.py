from django.shortcuts import render
from django.views.generic import TemplateView
from authors.models import Author
from books.models import Book


class HomePage(TemplateView):
    template_name="home/index.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['books'] = Book.objects.all()
        return context

def index(request):
    return render(request, 'home/index.html')