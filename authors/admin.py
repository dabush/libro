from django.contrib import admin

from .models import Author, School, Region

admin.site.register(School)
admin.site.register(Region)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'slug', 'featured_author')
	list_filter = ('date_added', 'featured_author')
	search_fields = ('last_name', 'first_name', 'country', 'bio')
	prepopulated_fields = {'slug': ('first_name','last_name'), 'full_name': ('first_name', 'last_name')}
	date_hierarchy = 'date_added'