from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from authors.models import Author
from books.models import Book
from books.serializers import BookSerializer


class HomePage(TemplateView):
    template_name="home/index.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['featuredauthors'] = Author.objects.filter(featured_author=True)
        context['featuredbooks'] = Book.objects.filter(book_featured=True)
        return context

def index(request):
    return render(request, 'home/index.html')

class BookViewSet(APIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def list(self, request):
		queryset = self.Book.objects.all()
		serializer = BookSerializer(self.get_queryset(), many=True)
		return Response(serializer.data)