from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile, UserList, UserListEntry
from books.models import Book

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	password= forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth', 'photo')

class UserListCreateForm(forms.ModelForm):
	user = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=get_user_model().objects.all(), disabled=True)
	name = forms.CharField(max_length=150)
	list_desc = forms.CharField(max_length=500, widget=forms.Textarea)
	list_image = forms.ImageField(required=False)

	class Meta:
		model = UserList
		fields = ['user', 'name', 'list_desc', 'list_image']

class UserEntryAddForm(forms.ModelForm):
	user = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=get_user_model().objects.all(), disabled=True)
	book = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Book.objects.all(), disabled=True)
	user_list = forms.ModelChoiceField(widget=forms.Select, queryset=UserList.objects.all(), empty_label=None)

	class Meta:
		model = UserListEntry
		fields = ['user', 'book', 'user_list']