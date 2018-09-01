from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
	author = serializers.StringRelatedField()
	absolute_url = serializers.URLField(source = 'get_absolute_url', read_only=True)
	class Meta:
		model = Book
		fields = '__all__'