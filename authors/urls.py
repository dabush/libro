from django.urls import path
from django.conf.urls import include
from . import views
from .views import AuthorPage, AuthorDetailPage

app_name = 'authors'
urlpatterns = [
    path('', AuthorPage.as_view(), name='home'),
    path('<slug:slug>,<int:author_id>/', AuthorDetailPage.as_view(), name='detail'),
]