from .models import Author
import django_filters

class AuthorFilter(django_filters.FilterSet):
	last_name = django_filters.CharFilter(lookup_expr='istartswith')
	class Meta:
		model = Author
		fields = ['last_name',]