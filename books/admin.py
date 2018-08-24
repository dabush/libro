from django.contrib import admin

from .models import Book, Theme, Genre, Form, Period


admin.site.register(Theme)
admin.site.register(Genre)
admin.site.register(Form)
admin.site.register(Period)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('book_title', 'author', 'slug', 'book_featured')
	list_filter = ('author', 'book_featured')
	search_fields = ('book_title', 'author', 'book_desc')
	prepopulated_fields = {'slug': ('book_title',)}
	date_hierarchy = 'pub_date'