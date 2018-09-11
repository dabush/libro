from django.urls import path, include
from . import views
from .views import UserListFormView, UserListView, UserListEntryDeleteView, UserListDeleteView
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.dashboard, name='dashboard'),
	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('', include('django.contrib.auth.urls')),
	path('register/', views.register, name='register'),
	path('edit/', views.edit, name='edit'),
	path('create-list/', UserListFormView.as_view(), name='create_user_list'),
	path('<int:pk>/delete-list/', UserListDeleteView.as_view(), name='delete_user_list'),
	path('lists/<int:userlist_id>', UserListView.as_view(), name='user_list_view'),
	path('lists/<int:userlist_id>/<int:pk>/delete', UserListEntryDeleteView.as_view(), name='user_list_entry_delete_view'),
]