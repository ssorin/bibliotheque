# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from biblio.models import Series


def series_detail(request, series_id):
    """
    Page détail d'une série
    Affiche les informations de la serie ainsi que les livres qu'elle contient
    """
    series = get_object_or_404(Series, pk=series_id)

    return render(request, "biblio/series_detail.html", {'series': series})


def series_list(request):
    """
    Liste toutes les séries
    """
    series = Series.objects.all()

    return render(request, "biblio/series_list.html", {'series': series})
