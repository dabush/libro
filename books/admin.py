from django.contrib import admin

from .models import Book, Theme, Genre, Form, Period, Rating, BookList, ListEntry


admin.site.register(Theme)
admin.site.register(Genre)
admin.site.register(Form)
admin.site.register(Period)
admin.site.register(Rating)

class ListEntryInline(admin.TabularInline):
	model = ListEntry
	extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('book_title', 'slug', 'book_featured')
	list_filter = ('author', 'book_featured')
	#search_fields = ('book_title__name', 'author__field_1', 'book_desc__field_2')
	prepopulated_fields = {'slug': ('book_title',)}
	date_hierarchy = 'pub_date'
	inlines = (ListEntryInline,)

@admin.register(BookList)
class BookListAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	inlines = (ListEntryInline,)