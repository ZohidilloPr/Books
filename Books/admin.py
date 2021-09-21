from django.contrib import admin
from .models import Book, Authors
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('author','book_name', 'book_cover', 'have_book_cover')

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'birth_date',)

admin.site.register(Authors, AuthorAdmin)