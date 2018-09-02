from django.forms import ModelForm, Textarea
from .models import Rating

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'user_rating', 'book']