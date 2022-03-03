# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from biblio.models import Category


@login_required
def category_detail(request, category_id):
    """
    Page détail d'une catégorie
    Affiche les livres d'une catégorie en particulier
    """
    category = get_object_or_404(Category, pk=category_id)

    return render(request, "biblio/default_detail.html", {'obj': category})


@login_required
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
