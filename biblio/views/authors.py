# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from biblio.models import Author


def author_detail(request, author_id):
    """
    Page détail d'un auteur
    Affiche les informations de l'auteur ainsi que les livres dont il est l'auteur
    """
    author = get_object_or_404(Author, pk=author_id)

    return render(request, "biblio/author_detail.html", {'author': author})


def author_list(request):
    """
    Liste tous les auteurs de la collection
    """
    authors = Author.objects.all()

    return render(request, "biblio/author_list.html", {'authors': authors})
