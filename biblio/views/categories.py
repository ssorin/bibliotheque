# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from biblio.models import Category


def category_detail(request, category_id):
    """
    Page détail d'une catégorie
    Affiche les livres d'une catégorie en particulier
    """
    category = get_object_or_404(Category, pk=category_id)

    return render(request, "biblio/default_detail.html", {'obj': category})


def category_list(request):
    """
    Liste toutes les catégories
    """
    categories = Category.objects.all()

    return render(
        request, "biblio/default_list.html",
        {
            'objects': categories,
            'page_title': 'Catégories'
        }
    )
