# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from biblio.models import Edition

def edition_detail(request, edition_id):
    """
    Page détail d'une catégorie
    Affiche les livres d'une catégorie en particulier
    """
    edition = get_object_or_404(Edition, pk=edition_id)

    return render(request, "biblio/edition_detail.html", {'edition': edition})


def edition_list(request):
    """
    Liste toutes les catégories
    """
    editions = Edition.objects.all()

    return render(request, "biblio/edition_list.html", {'editions': editions})
