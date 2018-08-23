from django.contrib import admin

from .models import Book, Theme, Genre, Form, Period

admin.site.register(Book)
admin.site.register(Theme)
admin.site.register(Genre)
admin.site.register(Form)
admin.site.register(Period)