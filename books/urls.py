from django.urls import path
from django.conf.urls import include
from . import views
from .views import BookPage, BookDetailPage

app_name = 'books'
urlpatterns = [
    path('', BookPage.as_view(), name='home'),
    path('<slug:slug>,<int:book_id>/', BookDetailPage.as_view(), name='book_detail'),
    path('<slug:slug>,<int:book_id>/like/', views.book_like, name='like'),
    path('browse/', views.book_list, name='list'),
]