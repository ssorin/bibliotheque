from django.contrib import admin
from .models import Category, Edition, Book, Author, BookType, AuthorType, Series


admin.site.register(Author)
admin.site.register(Edition)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BookType)
admin.site.register(AuthorType)
admin.site.register(Series)
