import datetime
from haystack import indexes
from .models import Author


class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    last_name = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(use_template=True)
    country = indexes.CharField(use_template=True)
    author = indexes.CharField(model_attr='user')
    date_of_birth = indexes.DateTimeField(model_attr='date_of_birth')

    def get_model(self):
        return Author

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())