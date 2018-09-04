from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Rating, Book

class RatingForm(ModelForm):

	user = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=get_user_model().objects.all(), disabled=True)
	book = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Book.objects.all(), disabled=True)
	value = forms.ChoiceField(label='Rate', widget=forms.RadioSelect, choices=Rating.RATING_CHOICES)

	class Meta:
		model = Rating
		fields = ['value', 'user', 'book']
