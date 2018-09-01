from rest_framework import routers
from books.viewsets import BookViewSet
from authors.viewsets import AuthorViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)