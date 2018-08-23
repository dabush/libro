from django.urls import path
from django.conf.urls import include
from . import views
from .views import HomePage

app_name = 'home'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]