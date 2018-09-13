from django.urls import path
from django.conf.urls import include
from django_filters.views import FilterView
from .filters import AuthorFilter
from . import views
from .views import AuthorPage, AuthorDetailPage, BrowseAllAuthorsPage, AllLists, AuthorListsOfKind, GenericAuthorList

app_name = 'authors'
urlpatterns = [
    path('', AuthorPage.as_view(), name='home'),
    path('<slug:slug>,<int:author_id>/', AuthorDetailPage.as_view(), name='detail'),
    path('<slug:slug>,<int:author_id>/like/', views.author_like, name='like'),
    path('browse/', views.author_list, name='browse'),
    path('browse/filter/', FilterView.as_view(filterset_class=AuthorFilter, template_name='authors/list1.html'), name='author_filter'),
    path('lists/', AllLists.as_view(), name='author_lists'),
    path('lists/<str:kind>/', AuthorListsOfKind.as_view(), name='author_lists_of_kind'),
    path('lists/<str:kind>/<slug:slug>,<int:authorlist_id>/', GenericAuthorList.as_view(), name='generic_author_list'),
]