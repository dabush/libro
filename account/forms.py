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
	not_public = forms.BooleanField(label='Would you like this list to be private?', required=False)
	name = forms.CharField(label='A name for your list' , max_length=150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Books Nietzsche would approve of..'}))
	list_desc = forms.CharField(label='A description of your list',max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
	list_image = forms.ImageField(label='A picture for your list', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

	class Meta:
		model = UserList
		fields = ['user', 'name', 'not_public', 'list_desc', 'list_image']

class UserEntryAddForm(forms.ModelForm):
	user = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=get_user_model().objects.all(), disabled=True)
	book = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Book.objects.all(), disabled=True)
	user_list = forms.ModelChoiceField(label=False, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}), queryset=UserList.objects.all(), empty_label=None)

	def __init__(self, user, *args, **kwargs):
		super(UserEntryAddForm, self).__init__(*args, **kwargs)
		self.fields['user_list'].queryset = UserList.objects.filter(user=user)

	class Meta:
		model = UserListEntry
		fields = ['user', 'book', 'user_list']