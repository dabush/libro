from django.urls import path
from django.conf.urls import include
from . import views
from .views import BookPage, BookDetailPage, RatingFormView, UpdateRatingFormView

app_name = 'books'
urlpatterns = [
    path('', BookPage.as_view(), name='home'),
    path('<slug:slug>,<int:book_id>/', BookDetailPage.as_view(), name='book_detail'),
    path('<slug:slug>,<int:book_id>/like/', views.book_like, name='like'),
    path('<slug:slug>,<int:book_id>/rate/', RatingFormView.as_view(), name='rate'),
    path('<slug:slug>,<int:book_id>/rate/<int:pk>', UpdateRatingFormView.as_view(), name='update_rating'),
    path('browse/', views.book_list, name='list'),
]