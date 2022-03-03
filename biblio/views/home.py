# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from biblio.models import Book


@login_required
def index(request):
    """ Page d'accueil de l'application biblio """

    last_books_add = Book.objects.order_by()[:5]

    return render(request, "biblio/home.html", {'books': last_books_add})
