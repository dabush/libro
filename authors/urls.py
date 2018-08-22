from django.urls import path

from . import views

app_name = 'authors'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:author_id>/', views.detail, name='detail'),
]