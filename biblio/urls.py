from django.urls import path

from .views.authors import author_detail, author_list
from .views.book_types import book_type_detail, book_type_list
from .views.books import book_list, book_detail
from .views.categories import category_list, category_detail
from .views.editions import edition_detail, edition_list
from .views.series import series_list, series_detail
from .views.home import index


app_name = 'biblio'
urlpatterns = [
    path('books/<int:book_id>', book_detail, name='book_detail'),
    path('books/', book_list, name='book_list'),

    path('authors/<int:author_id>', author_detail, name='author_detail'),
    path('authors/', author_list, name='author_list'),

    path('series/<int:series_id>', series_detail, name='series_detail'),
    path('series/', series_list, name='series_list'),

    path('book-types/<int:book_type_id>', book_type_detail, name='book_type_detail'),
    path('book-types/', book_type_list, name='book_types_list'),

    path('categories/<int:category_id>', category_detail, name='category_detail'),
    path('categories/', category_list, name='category_list'),

    path('editions/<int:edition_id>', edition_detail, name='edition_detail'),
    path('editions/', edition_list, name='edition_list'),

    path('', index, name='home'),
]