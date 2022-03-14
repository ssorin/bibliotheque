from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings

from biblio.models import Book


@login_required
def home(request):
    """
    Page d'accueil du site
    """

    books = Book.objects.all()
    last_books_add = books.order_by('-create_date')[:5]

    return render(request, "home.html", {'last_books':last_books_add, 'books': books})
