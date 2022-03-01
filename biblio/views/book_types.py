# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from biblio.models import BookType


def book_type_detail(request, book_type_id):
    """
    Page détail d'un BookType
    Affiche les livres d'un BookType en particulier
    """
    book_type = get_object_or_404(BookType, pk=book_type_id)

    return render(request, "biblio/default_detail.html", {'obj': book_type})

def book_type_list(request):
    """
    Liste tous les BookType
    """
    book_types = BookType.objects.all()

    return render(
        request, "biblio/default_list.html",
        {
            'objects': book_types,
            'page_title': 'Types'
        }
    )
