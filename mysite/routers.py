from rest_framework import routers
from books.viewsets import BookViewSet
router = routers.DefaultRouter()
router.register(r'book', BookViewSet)