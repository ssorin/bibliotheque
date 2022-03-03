# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from biblio.models import Series


@login_required
def series_detail(request, series_id):
    """
    Page détail d'une série
    Affiche les informations de la serie ainsi que les livres qu'elle contient
    """
    series = get_object_or_404(Series, pk=series_id)

    return render(request, "biblio/default_detail.html", {'obj': series})


@login_required
def series_list(request):
    """
    Liste toutes les séries
    """
    series = Series.objects.all()

    return render(
        request, "biblio/default_list.html",
        {
            'objects': series,
            'page_title': 'Collections/Series'
        }
    )
