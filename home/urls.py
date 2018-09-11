from django.urls import path
from django.conf.urls import include
from . import views
from .views import HomePage, AllLists

app_name = 'home'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('lists/', AllLists.as_view(), name='all_lists_home')
]