from django.contrib import admin
from .models import Profile, UserList, UserListEntry

# Register your models here.


class UserListEntryInline(admin.TabularInline):
	model = UserListEntry
	extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'photo']


@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
	inlines = (UserListEntryInline,)