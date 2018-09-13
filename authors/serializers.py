from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
	book_to_author = serializers.StringRelatedField(many=True, read_only=True)
	absolute_url = serializers.URLField(source = 'get_absolute_url', read_only=True)
	country = CountryField(country_dict=True)
	class Meta:
		model = Author
		fields = ('book_to_author', 'absolute_url', 'first_name', 'last_name', 'full_name', 'country')