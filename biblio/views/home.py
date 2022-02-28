# -*- coding: utf-8 -*-
from django.shortcuts import render

from biblio.models import Book


def index(request):
    """ Page d'accueil de l'application biblio """

    last_books_add = Book.objects.order_by()[:5]

    return render(request, "biblio/home.html", {'books': last_books_add})
