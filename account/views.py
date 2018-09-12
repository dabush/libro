from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, UserListCreateForm, UserEntryAddForm
from .models import Profile, UserList, UserListEntry
# from .mixins import PermissionMixin

from books.mixins import AjaxFormMixin
from books.models import Book, Rating
from authors.models import Author

# Create your views here.
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request,
								username=cd['username'],
								password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated succesfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request,'account/login.html', {'form': form})

@login_required
def dashboard(request):
	liked_authors = request.user.author_likes.all()
	user = request.user
	user_ratings = Rating.objects.filter(user=request.user).order_by('-value')
	user_lists = UserList.objects.filter(user=request.user)
	new_user_list = UserListCreateForm
	form_url = reverse('accounts:create_user_list')
	return render(request, 'account/dashboard.html', {'user': user, 'section': dashboard, 'user_ratings': user_ratings, 'user_lists': user_lists, 'liked_authors': liked_authors, 'new_user_list': new_user_list, 'form_url': form_url})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			#create a new user but avoid saving it yet
			new_user = user_form.save(commit=False)
			#set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			#save the user object
			new_user.save()
			Profile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully')
		else:
			messages.error(request, 'Error updating your profile')
	else: 
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form })

class UserListFormView(AjaxFormMixin, FormView):
	def get_initial(self):
		initial = super().get_initial()
		initial['user'] = self.request.user.id
		return initial

	form_class = UserListCreateForm
	template_name  = 'account/_list_create.html'
	success_url = '/accounts/'

class UserListView(TemplateView):
	template_name = 'account/list.html'
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		userlist = UserList.objects.get(id=self.kwargs['userlist_id'])
		context['userlist'] = userlist
		context['list_entries'] = UserListEntry.objects.filter(user_list=userlist)
		context['delete_url'] = reverse('accounts:delete_user_list', kwargs={'pk': userlist.id })
		context['edit_form'] = UserListCreateForm
		return context

class UserListEntryDeleteView(AjaxFormMixin, UserPassesTestMixin, DeleteView):
	model = UserListEntry
	template_name = 'account/_listentry_delete.html'
	success_url = reverse_lazy('accounts:dashboard')

	def test_func(self):
		self.object = self.get_object()
		return self.request.user == self.object.user

class UserListUpdateView(AjaxFormMixin, UserPassesTestMixin, UpdateView):

	def test_func(self):
		self.object = self.get_object()
		return self.request.user == self.object.user

	def get_initial(self):
	#Return the initial data to use for forms on this view.
		return self.initial.copy()

	model = UserList
	fields = ('name', 'not_public', 'list_desc', 'list_image',)
	template_name = 'account/_list_edit.html'
	userlist_id_url_kwarg = 'userlist_id'
	context_object_name = 'userlist'


class UserListDeleteView(AjaxFormMixin, UserPassesTestMixin, DeleteView):
	model = UserList
	template_name = 'account/_list_delete.html'
	success_url = reverse_lazy('accounts:dashboard')

	def test_func(self):
		self.object = self.get_object()
		return self.request.user == self.object.user