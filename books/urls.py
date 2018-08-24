from django.urls import path
from django.conf.urls import include
from . import views
from .views import BookPage, BookDetailPage, BrowseAllBooksPage


app_name = 'books'
urlpatterns = [
    path('', BookPage.as_view(), name='home'),
    path('<slug:slug>,<int:book_id>/', BookDetailPage.as_view(), name='detail'),
    path('browse/', BrowseAllBooksPage.as_view(), name='browse'),
]