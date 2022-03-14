from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from biblio.models import Book


@login_required
def home(request):
    """
    Page d'accueil du site
    """

    books = Book.objects.all()
    last_books_add = books.order_by('-create_date')[:5]

    return render(request, "home.html", {'last_books':last_books_add, 'books': books})
