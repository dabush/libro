from django.urls import path
from django.conf.urls import include
from . import views
from .views import BookPage, BookDetailPage, RatingFormView, UpdateRatingFormView, AllLists, ListsOfKind, GenericList, UserListEntryView

app_name = 'books'
urlpatterns = [
    path('', BookPage.as_view(), name='home'),
    path('<slug:slug>,<int:book_id>/', BookDetailPage.as_view(), name='book_detail'),
    path('<slug:slug>,<int:book_id>/rate/', RatingFormView.as_view(), name='rate'),
    path('<slug:slug>,<int:book_id>/rate/<int:pk>', UpdateRatingFormView.as_view(), name='update_rating'),
    path('browse/', views.book_list, name='list'),
    path('lists/', AllLists.as_view(), name='all_lists'),
    path('lists/<str:kind>/', ListsOfKind.as_view(), name='lists_of_kind'),
    path('lists/<str:kind>/<slug:slug>,<int:booklist_id>/', GenericList.as_view(), name='generic_list'),
    path('<slug:slug>,<int:book_id>/add/', UserListEntryView.as_view(), name='user_list_add'),
]