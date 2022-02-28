# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from biblio.models import Book


def book_detail(request, book_id):
    """
    Page de détail d'un livre
    """
    book = get_object_or_404(Book, pk=book_id)

    return render(request, "biblio/book_detail.html", {'book': book})


def book_list(request):
    """
    Liste tous les livres de la collection
    """

    books = Book.objects.all()

    return render(request, "biblio/book_list.html", {'books': books})